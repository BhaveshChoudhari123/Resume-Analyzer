import os
import resend

resend.api_key = os.getenv("RESEND_API_KEY")


def send_otp_email(to_email, otp, subject):

    resend.Emails.send({
        "from": "Resume Analyzer <onboarding@resend.dev>",
        "to": [to_email],
        "subject": subject,
        "html": f"""
        <h2>Resume Analyzer</h2>

        <p>Your OTP is:</p>

        <h1>{otp}</h1>

        <p>This OTP is valid for 5 minutes.</p>
        """
    })