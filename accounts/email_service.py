import os
import resend

resend.api_key = os.getenv("RESEND_API_KEY")


def send_otp_email(email, otp, subject):

    resend.Emails.send({
        "from": "Resume Analyzer <onboarding@resend.dev>",
        "to": email,
        "subject": subject,
        "html": f"""
        <h2>Resume Analyzer</h2>

        <p>Your OTP is:</p>

        <h1>{otp}</h1>

        <p>This OTP expires in 5 minutes.</p>
        """
    })