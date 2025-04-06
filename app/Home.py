# -*- coding: utf-8 -*-

"""This module handles UI home page."""

import streamlit as st

st.set_page_config(page_title="app", page_icon="🩺", layout="wide")

st.title("Welcome to app")
st.write(
    """
**app** is a medical assistant tool designed to help you with the following features:
- **Symptom Checker**: Enter symptoms and get a potential diagnosis.
- **Health Report Summarizer**: Upload a blood report (PDF) to analyze potential conditions.
"""
)
st.sidebar.success("Select a feature from the menu.")
