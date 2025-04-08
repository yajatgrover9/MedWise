# MedWise: AI-Powered Healthcare Application

## Overview
MedWise is an AI-powered healthcare application designed to assist users in analyzing medical symptoms and summarizing blood reports. It leverages **Google Gemini AI** to provide potential diagnoses and medical advice based on uploaded reports and symptoms.

## Features
- **Authentication System:** Login with username and password to access the application securely.
- **Symptom Checker:** Users can input symptoms, and the AI provides potential diagnoses.
- **Blood Report Summarizer:** Upload a blood report (PDF), and the AI extracts and summarizes key findings.
- **User-Friendly Interface:** Built with **Streamlit** for an interactive and easy-to-use experience.

## Tech Stack
- **Python**
- **Streamlit** (Frontend UI)
- **Google Generative AI (Gemini 1.5-Flash)** (AI-powered analysis)
- **PyPDF2** (PDF text extraction)

## Installation
### Prerequisites
- Python 3.8+
- Google Generative AI API Key

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yajatgrover9/MedWise
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google Generative AI API key**
   - Obtain an API key from Google Generative AI.
   - Create a `.env` file and add:
     ```env
     GOOGLE_GENAI_KEY=your_api_key_here
     ```
   - User login credentials and authentication logic is managed securely using a ```config.yaml``` file.


5. **Run the Streamlit app**
   ```bash
   streamlit run app/Home.py
   ```

## Usage
### Symptom Checker
1. Open the application.
2. Enter patient details and symptoms.
3. Click **Submit** to get AI-powered diagnosis suggestions.

### Blood Report Summarizer
1. Upload a **PDF** blood report.
2. Click **Submit** after text extraction.
3. View AI-generated summary and possible medical conditions.

## Project Structure
```
Medwise/
├── app/
│   ├── pages/
│      ├── 1_SymptomChecker.py
│      ├── 2_HealthSummarizer.py
│   ├── genai_services.py
│   ├── Home.py
├── requirements.txt
├── README.md
└── .env
```
## 🚀 Live Application

MedWise is live and ready to use! You can access the deployed version of the app here:

🔗 **Launch [MedWise](https://medwise-ai.streamlit.app)**

### Authentication Notice:
To ensure privacy and data security, MedWise requires **login authentication** before using any features. Only authorized users can access symptom analysis or upload medical reports.
If you’d like to use the MedWise application, please reach out to the admin.

## Future Improvements
- Integration with **FHIR APIs** for better medical data handling.
- Improved symptom selection via **searchable dropdowns**.
- Enhanced AI responses using **fine-tuned medical models**.

## Contributing

We welcome contributions to MedWise!

To maintain stability and security of the deployed application, all contributions should be made using [**`dev` branch**](https://github.com/yajatgrover9/MedWise/tree/dev) only.

### Steps to Contribute:

1. **Clone the repository and checkout the `dev` branch**:
```bash
   git clone -b dev https://github.com/yajatgrover9/MedWise.git
   cd MedWise
```
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request for ```dev```.

## Contact
For inquiries or support, reach out to **yajatgrover@gmail.com**
