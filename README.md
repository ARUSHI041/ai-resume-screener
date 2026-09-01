# Resume Screener AI

An AI-powered resume screening web application built with Python and Flask.

The application analyzes a candidate's resume against a given job description, calculates a keyword-based match score, identifies matched and missing skills, and provides suggestions to improve the resume.

## Features

- Upload resume in PDF format
- Extract resume text using PyMuPDF
- Compare resume skills with job description
- Calculate resume-to-job match percentage
- Identify matched skills
- Identify missing skills
- Provide resume improvement suggestions
- Optional Recruiter Mode for sending screening results through email
- Secure uploaded filenames
- Automatic deletion of uploaded resumes after processing
- Input validation and error handling
- Responsive web interface

## Tech Stack

- Python
- Flask
- PyMuPDF
- HTML5
- CSS3
- JavaScript
- SMTP
- Git & GitHub

## Project Structure

    resume_screener_ai/
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    │
    ├── templates/
    │   ├── index.html
    │   └── result.html
    │
    ├── static/
    │   ├── style.css
    │   └── loader.gif
    │
    ├── utils/
    │   ├── pdf_parser.py
    │   ├── keyword_matcher.py
    │   ├── suggestion_engine.py
    │   └── email_sender.py
    │
    └── uploads/

## How It Works

    Candidate Resume (PDF)
              │
              ▼
        PDF Text Extraction
              │
              ▼
       Resume Skill Detection
              │
              ▼
         Job Description
              │
              ▼
       Skill Comparison Engine
              │
              ▼
          Match Score
              │
         ┌────┴────┐
         ▼         ▼
      Matched    Missing
       Skills     Skills
         │         │
         └────┬────┘
              ▼
       Improvement Suggestions
              │
              ▼
          Result Dashboard

## Installation

### 1. Clone the repository

    git clone <your-github-repository-url>

### 2. Navigate to the project

    cd resume_screener_ai

### 3. Create a virtual environment

    python -m venv venv

### 4. Activate the virtual environment

Windows:

    venv\Scripts\activate

### 5. Install dependencies

    pip install -r requirements.txt

### 6. Run the application

    python app.py

Open the application in your browser:

    http://127.0.0.1:5000

## Recruiter Mode Configuration

Recruiter Mode uses Gmail SMTP to send screening results.

For security, email credentials should not be stored directly in the source code.

Set the following environment variables:

    SENDER_EMAIL
    SENDER_APP_PASSWORD

Never commit passwords, API keys, or other credentials to GitHub.

## Example

A resume containing:

    Python
    SQL
    Power BI
    Excel
    Data Analysis

can be compared with a job description requiring:

    Python
    SQL
    Power BI
    Excel
    Data Analysis
    Tableau

The application identifies:

### Matched Skills

- Python
- SQL
- Power BI
- Excel
- Data Analysis

### Missing Skill

- Tableau

The application then calculates the corresponding resume-to-job match percentage and provides improvement suggestions.

## Limitations

The current version uses a predefined technical skill list and keyword-based matching.

Therefore, it may not fully understand:

- Synonyms
- Contextual meaning
- Transferable skills
- Semantic similarity
- Different wording of the same skill

## Future Improvements

- NLP-based semantic matching
- Improved skill extraction
- Resume section detection
- Experience and education analysis
- Weighted skill scoring
- Job-role specific skill detection
- Database integration
- Recruiter dashboard
- Authentication
- Resume analytics and visualizations

## Security

The project follows basic security practices including:

- Secure uploaded filenames
- PDF file validation
- Temporary resume processing
- Automatic deletion of uploaded resumes
- Environment variables for email credentials
- .gitignore for sensitive and local files

## Author

**Arushi Srivastava**

B.Tech Information Technology

This project was developed as a practical demonstration of Python, Flask, PDF document processing, keyword-based resume analysis, and web application development.