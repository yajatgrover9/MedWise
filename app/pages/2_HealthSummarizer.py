# -*- coding: utf-8 -*-

import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from genai_services import genai_response

authentication_status = st.session_state.get("authentication_status")
if authentication_status:
    st.title("Health Report Summarizer")
    st.write(
        "Upload a blood report (PDF format) to get a summary and potential diagnosis."
    )

    uploaded_file = st.file_uploader("Upload your blood report (PDF)", type="pdf")

    if uploaded_file:
        pdf_text = ""
        try:
            pdf_reader = PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                pdf_text += page.extract_text() + "\n"
            if pdf_text:
                st.success("PDF successfully uploaded and text extracted!")
                st.write("### Extracted Text:")
                st.text_area("Extracted Text", pdf_text, height=200)
            else:
                st.error("Could not extract text from the uploaded PDF.")

            if st.button("Submit for Diagnosis"):
                with st.spinner("Please Wait..."):
                    prompt = (
                        "You are a highly knowledgeable medical AI specializing in analyzing blood reports to detect blood-related diseases "
                        "and health conditions. Here is the full content of the patient's blood report:\n\n"
                        f"{pdf_text}\n\n"
                        "Based on this report, identify any possible blood-related diseases or health risks the patient may have. "
                        "Provide a summary including any detected conditions and relevant advice for the patient."
                    )
                    try:
                        model = genai.GenerativeModel("gemini-1.5-flash")
                        response = genai_response(prompt)
                        st.write("### AI-Generated Summary:")
                        st.write(response)
                    except Exception as e:
                        st.error(f"Error generating summary: {str(e)}")

        except Exception as e:
            st.error(f"Error processing the file: {str(e)}")
else:
    st.error("RESTRICTED")
    st.info("Use Home page to LOGIN")
