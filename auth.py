import streamlit as st

USERNAME = "admin"
PASSWORD = "soc123"

def login():
    st.title("🔐 SOC Dashboard Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
            st.success("Login successful")
        else:
            st.error("Invalid credentials")


def require_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login()
        st.stop()