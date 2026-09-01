import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(recipient_email, match_score, shortlisted):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_APP_PASSWORD")

    if not sender_email or not sender_password:
        print("Email credentials are not configured.")
        return False

    subject = "Resume Screening Result"

    if shortlisted:
        result_text = "You are shortlisted for the next round."
    else:
        result_text = (
            "Unfortunately, your resume did not match the job description "
            "closely. Please improve and try again."
        )

    body = f"""
Dear Candidate,

Thank you for applying.

Based on our resume screening analysis, your resume matches
{match_score}% with the job description.

{result_text}

Best regards,
Resume Screener AI Team
"""

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"Email sent successfully to {recipient_email}")
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False