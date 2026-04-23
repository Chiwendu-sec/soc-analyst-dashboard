import streamlit as st
import socket
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

from auth import require_login
from scanner import scan_target
from history import save_history, load_history
from report_utils import save_json_report

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="SOC SIEM Dashboard",
    page_icon="🛡",
    layout="wide"
)

# =========================
# DARK SIEM THEME
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: #ffffff;
}

/* Make login box centered & not too wide (MOBILE FRIENDLY) */
div[data-testid="stForm"] {
    max-width: 400px;
    margin: auto;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Buttons */
.stButton>button {
    background-color: #1f2937;
    color: white;
    border-radius: 8px;
    border: 1px solid #374151;
    width: 100%;
}

/* Inputs */
input {
    background-color: #111827 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user" not in st.session_state:
    st.session_state["user"] = None

# =========================
# LOGIN SYSTEM (CENTERED / MOBILE FRIENDLY)
# =========================
if not st.session_state["logged_in"]:
    st.title("🛡 SOC SIEM LOGIN")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

    if login_btn:
        if username == "admin" and password == "soc123":
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()

# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.title("🛡 SIEM CONTROL PANEL")

menu = st.sidebar.radio(
    "Navigation",
    ["🔍 Network Scan", "📊 Analytics", "📜 History", "⚙ Settings"]
)

st.sidebar.markdown("---")
st.sidebar.write(f"Logged in as: **{st.session_state['user']}**")

if st.sidebar.button("Logout"):
    st.session_state["logged_in"] = False
    st.session_state["user"] = None
    st.rerun()

# =========================
# SCANNER LOGIC
# =========================
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        s.close()
        if result == 0:
            return port
    except:
        pass
    return None

def run_scan(target):
    ports = [21, 22, 23, 53, 80, 443, 445, 3389]
    open_ports = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(target, p), ports)

    for r in results:
        if r:
            open_ports.append(r)

    return open_ports

# =========================
# MAIN TITLE
# =========================
st.title("🛡 SOC SIEM DASHBOARD")
st.markdown("---")

# =========================
# NETWORK SCAN PAGE
# =========================
if menu == "🔍 Network Scan":

    st.subheader("Network Vulnerability Scanner")

    target = st.text_input("Enter Target IP / Domain")

    if st.button("Start Scan"):

        if not target:
            st.warning("Please enter a target")
        else:
            st.info("Scanning in progress...")

            open_ports = run_scan(target)

            st.success("Scan Completed")

            # Convert to table (FIXED STRUCTURE)
            if open_ports:
                data = []

                for port in open_ports:
                    if port in [21, 23, 445, 3389]:
                        risk = "HIGH"
                    else:
                        risk = "MEDIUM"

                    data.append({
                        "Port": port,
                        "Risk Level": risk
                    })

                df = pd.DataFrame(data)

                st.error("⚠ Open Ports Detected")
                st.dataframe(df)

            else:
                st.success("🟢 No critical ports found")

# =========================
# ANALYTICS PAGE
# =========================
elif menu == "📊 Analytics":

    st.subheader("Threat Analytics")

    st.info("Analytics module (upgrade point)")

    st.write("""
    Future upgrades:
    - Risk charts
    - Attack patterns
    - Historical trends
    """)

# =========================
# HISTORY PAGE
# =========================
elif menu == "📜 History":

    st.subheader("Scan History")

    st.info("Stored scan results will appear here")

# =========================
# SETTINGS PAGE
# =========================
elif menu == "⚙ Settings":

    st.subheader("System Settings")

    st.write("User: ", st.session_state["user"])
    st.write("Environment: SOC Simulation Mode")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("SOC SIEM Simulation Dashboard")