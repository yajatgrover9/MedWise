# -*- coding: utf-8 -*-

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="MedWise", page_icon="🩺", layout="wide")

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

st.title("Welcome to MedWise 🩺")
authenticator.login(key="Login", location="main")

name = st.session_state.get("name")
username = st.session_state.get("username")
authentication_status = st.session_state.get("authentication_status")

details = {
    "name": name,
    "username": username,
    "authentication_status": authentication_status,
}
print(details)
if authentication_status is True and not st.session_state.get("logged_in_once", False):
    st.session_state["logged_in_once"] = True
    st.rerun()

if authentication_status is True:
    st.success(f"Welcome, {name}")
    st.write(
        """
    **MedWise** is a medical assistant tool designed to help you with the following features:
    - **Symptom Checker**: Enter symptoms and get a potential diagnosis.
    - **Health Report Summarizer**: Upload a blood report (PDF) to analyze potential conditions.
    """
    )
    st.sidebar.success("Select a feature from the menu.")
    authenticator.logout("Logout", "main")


if authentication_status is False:
    st.error("Incorrect username/password")
