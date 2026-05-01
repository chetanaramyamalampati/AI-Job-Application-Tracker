# AI-Job-Application-Tracker

## Project Overview
Track job applications, extract skills from job descriptions, visualize status, and generate AI follow-up emails.

## Features
- Clean Streamlit user interface
- Modular Python source code
- Sample data and reusable project structure
- Ready for GitHub upload
- Easy to extend with OpenAI, Gemini, Claude, or local models

## Tech Stack
streamlit, pandas, plotly, python-dotenv, openai

## Folder Structure
```text
AI-Job-Application-Tracker/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
├── src/
├── data/sample/
├── docs/
├── notebooks/
└── screenshots/
```

## Installation
```bash
git clone <your-repo-url>
cd AI-Job-Application-Tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

For Mac/Linux:
```bash
source venv/bin/activate
```

## Run the App
```bash
streamlit run app.py
```

## Environment Variables
Create a `.env` file using `.env.example`.

## Future Improvements
- Add authentication
- Add database storage
- Add better LLM integration
- Add Docker deployment
- Add unit tests
- Add cloud deployment on AWS/Azure/GCP

## Resume Bullet Point
Built `AI-Job-Application-Tracker`, an AI-powered application using Python, Streamlit, NLP/ML workflows, and modular backend services to automate real-world business tasks.
