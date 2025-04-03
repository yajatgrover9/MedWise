import streamlit as st

st.set_page_config(
    page_title="MedWise",
    page_icon="🩺",
    layout="wide"
)

st.title("Welcome to MedWise")
st.write("""
**MedWise** is a medical assistant tool designed to help you with the following features:
- **Symptom Checker**: Enter symptoms and get a potential diagnosis.
- **Health Report Summarizer**: Upload a blood report (PDF) to analyze potential conditions.
""")
st.sidebar.success("Select a feature from the menu.")
