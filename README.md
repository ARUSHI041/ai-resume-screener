# Resume Screener AI

A Python and Flask-based resume screening web application that analyzes a candidate's resume against a job description, calculates a keyword-based match score, identifies matched and missing skills, and provides resume improvement suggestions.

## Features

* Upload resumes in PDF format
* Extract resume text using PyMuPDF
* Compare resume skills with a job description
* Calculate resume-to-job match percentage
* Identify matched skills
* Identify missing skills
* Generate resume improvement suggestions
* Optional Recruiter Mode for sending screening results through email
* Secure uploaded filenames
* Automatic deletion of uploaded resumes after processing
* Input validation and error handling
* Responsive web interface

## Tech Stack

* Python
* Flask
* PyMuPDF
* HTML5
* CSS3
* JavaScript
* SMTP
* Git & GitHub

## Project Structure

```text
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
```

## How It Works

```text
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
      ┌───┴───┐
      ▼       ▼
   Matched   Missing
    Skills    Skills
      │       │
      └───┬───┘
          ▼
Improvement Suggestions
          │
          ▼
    Result Dashboard
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ARUSHI041/ai-resume-screener.git
```

### 2. Navigate to the project

```bash
cd ai-resume-screener
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Recruiter Mode Configuration

Recruiter Mode uses Gmail SMTP to send screening results.

For security, email credentials are not stored directly in the source code.

The application expects the following environment variables:

```text
SENDER_EMAIL
SENDER_APP_PASSWORD
```

Never commit passwords, API keys, or other credentials to GitHub.

> Note: Email configuration is optional. The core resume screening functionality works without configuring Recruiter Mode.

## Example

A resume containing:

```text
Python
SQL
Power BI
Excel
Data Analysis
```

can be compared with a job description requiring:

```text
Python
SQL
Power BI
Excel
Data Analysis
Tableau
```

The application identifies:

### Matched Skills

* Python
* SQL
* Power BI
* Excel
* Data Analysis

### Missing Skill

* Tableau

The application then calculates the corresponding resume-to-job match percentage and provides improvement suggestions.

## Limitations

The current version uses a predefined technical skill list and keyword-based matching.

Therefore, it may not fully understand:

* Synonyms
* Contextual meaning
* Transferable skills
* Semantic similarity
* Different wording of the same skill

## Future Improvements

* NLP-based semantic matching
* Improved skill extraction
* Resume section detection
* Experience and education analysis
* Weighted skill scoring
* Job-role specific skill detection
* Database integration
* Recruiter dashboard
* Authentication
* Resume analytics and visualizations

## Security

The project follows basic security practices including:

* Secure uploaded filenames
* PDF file validation
* Temporary resume processing
* Automatic deletion of uploaded resumes
* Environment variables for email credentials
* `.gitignore` for sensitive and local files

## Author

**Arushi Srivastava**

B.Tech Information Technology

This project was developed as a practical demonstration of Python, Flask, PDF document processing, keyword-based resume analysis, and web application development.
