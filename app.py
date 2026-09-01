from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from utils.pdf_parser import extract_text_from_pdf
from utils.keyword_matcher import get_matching_score
from utils.suggestion_engine import get_missing_keywords
from utils.email_sender import send_email


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        # Get uploaded resume
        file = request.files.get("resume")

        # Get job description
        jd_text = request.form.get("jd", "").strip()

        # Recruiter mode
        recruiter = request.form.get("recruiter") == "on"

        # Email
        email = request.form.get("email", "").strip()

        # Validate resume
        if not file or file.filename == "":
            return render_template(
                "index.html",
                error="Please upload a resume in PDF format."
            )

        if not allowed_file(file.filename):
            return render_template(
                "index.html",
                error="Only PDF files are allowed."
            )

        # Validate job description
        if not jd_text:
            return render_template(
                "index.html",
                error="Please enter a job description."
            )

        # Validate email only when recruiter mode is enabled
        if recruiter and not email:
            return render_template(
                "index.html",
                error="Please enter an email address for Recruiter Mode."
            )

        # Secure filename
        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        try:
            # Save uploaded resume
            file.save(filepath)

            # Extract text
            resume_text = extract_text_from_pdf(filepath)

            if not resume_text:
                return render_template(
                    "index.html",
                    error="Could not extract text from the PDF. Please upload a valid text-based PDF."
                )

            # Calculate matching score
            match_score, matched_keywords, unmatched_keywords = (
                get_matching_score(
                    resume_text,
                    jd_text
                )
            )

            # Generate suggestions
            suggestions = get_missing_keywords(
                unmatched_keywords,
                jd_text
            )

            # Shortlisting threshold
            shortlisted = match_score >= 60

            # Email status
            email_status = None

            if recruiter:
                email_status = send_email(
                    email,
                    match_score,
                    shortlisted
                )

            return render_template(
                "result.html",
                score=match_score,
                suggestions=suggestions,
                recruiter=recruiter,
                email=email,
                matched=matched_keywords,
                unmatched=unmatched_keywords,
                email_status=email_status
            )

        except Exception as e:
            print("Application error:", e)

            return render_template(
                "index.html",
                error="Something went wrong while processing the resume."
            )

        finally:
            # Remove uploaded file after processing
            if os.path.exists(filepath):
                os.remove(filepath)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)