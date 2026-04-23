import streamlit as st
from auth import require_login
from scanner import scan_target
from history import save_history, load_history
from report_utils import save_json_report

require_login()

st.title("🛡 SOC Port Scanner Dashboard")

target = st.text_input("Enter target IP or domain")

if st.button("Start Scan"):

    if target:
        st.info("Scanning...")

        results = scan_target(target)

        if results:
            st.success("Scan Complete")

            st.dataframe(results)

            # Save history + report
            save_history(target, results)
            file = save_json_report(target, results)

            st.success(f"Report saved: {file}")

            # Charts
            high = len([r for r in results if r["risk"] == "HIGH"])
            low = len([r for r in results if r["risk"] == "LOW"])

            st.subheader("📊 Risk Breakdown")
            st.bar_chart({"HIGH": high, "LOW": low})

        else:
            st.success("No open ports found")