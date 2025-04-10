# -*- coding: utf-8 -*-

import streamlit as st
from genai_services import genai_response

common_symptoms = [
    "Fatigue",
    "Weakness",
    "Fever",
    "Chills",
    "Night sweats",
    "Weight loss without trying",
    "Weight gain without trying",
    "Loss of appetite",
    "Excessive thirst",
    "Dehydration",
    "Headache",
    "Muscle pain",
    "Joint pain",
    "Chest pain",
    "Abdominal pain",
    "Back pain",
    "Sore throat",
    "Dizziness",
    "Fainting",
    "Tingling or numbness",
    "Difficulty concentrating",
    "Memory loss",
    "Seizures",
    "Vision problems",
    "Shortness of breath",
    "Persistent cough",
    "Rapid heartbeat",
    "Swelling in legs",
    "Nausea",
    "Vomiting",
    "Diarrhea",
    "Constipation",
    "Heartburn",
    "Rash",
    "Itching",
    "Frequent urination",
    "Painful urination",
    "Blood in urine",
]
authentication_status = st.session_state.get("authentication_status")
if authentication_status:
    st.title("Symptom Checker")
    st.write("Enter the patient's details and symptoms to get a potential diagnosis.")

    # Patient details
    patient_name = st.text_input("Patient Name")
    patient_age = st.number_input("Age", min_value=0, max_value=120, step=1)
    patient_gender = st.radio("Gender", options=["Male", "Female", "Other"])

    symptom_entry_method = st.radio(
        "How would you like to enter symptoms?",
        options=["Select from dropdown", "Type symptoms manually"],
    )

    if symptom_entry_method == "Select from dropdown":
        selected_symptoms = st.multiselect("Select Symptoms", common_symptoms)
        symptoms = ", ".join(selected_symptoms)
    else:
        symptoms = st.text_area(
            "Enter Symptoms (separated by commas)",
            placeholder="E.g., fever, headache, joint pain",
        )

    if st.button("Get Diagnosis"):
        with st.spinner("Please Wait ..."):
            if not patient_name or not symptoms:
                st.error("Please fill out all fields.")
            else:
                prompt = (
                    "You are an experienced medical professional specializing in diagnosing diseases based on symptoms. "
                    f"Patient Name: {patient_name}, Age: {patient_age}, Gender: {patient_gender}. "
                    f"The patient reports the following symptoms: {symptoms}. "
                    "Based on these symptoms, please provide a potential diagnosis and any recommendations."
                )

                response = genai_response(prompt)
                st.success("Diagnosis Completed!")
                st.write(f"### Diagnosis for {patient_name}")
                st.write(response)
else:
    st.error("RESTRICTED")
    st.info("Use Home page to LOGIN")
