import PyPDF2
import os
import hashlib

def extract_text_from_pdf(pdf_file):

    text = ""

    try:

        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:

        print("PDF ERROR:", e)

    return text


def get_skill_statistics(skills):

    if not skills:
        return 0

    percentage = len(skills) * 5

    return min(percentage, 100)


def get_resume_level(score):

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    else:
        return "Needs Improvement"


def calculate_resume_score(text, skills):

    score = 40  # Base score

    text = text.lower()

    # Skills
    score += len(skills) * 3

    # Resume Sections
    if "education" in text:
        score += 8

    if "project" in text:
        score += 10

    if "experience" in text:
        score += 10

    if "internship" in text:
        score += 10

    if "certification" in text:
        score += 8

    if "achievement" in text:
        score += 5

    if "github" in text:
        score += 5

    if "linkedin" in text:
        score += 4

    if len(text) > 1500:
        score += 5

    return min(score, 100)


def calculate_ats_score(text):

    ats_score = 50  # Base ATS

    text = text.lower()

    if "education" in text:
        ats_score += 8

    if "skills" in text:
        ats_score += 8

    if "project" in text:
        ats_score += 8

    if "experience" in text:
        ats_score += 8

    if "certification" in text:
        ats_score += 5

    if "github" in text:
        ats_score += 4

    if "linkedin" in text:
        ats_score += 4

    if len(text) > 1000:
        ats_score += 5

    return min(ats_score, 100)

def validate_resume_file(uploaded_file):

    # Allowed extension
    extension = os.path.splitext(
        uploaded_file.name
    )[1].lower()

    if extension != ".pdf":

        return False, "Only PDF resumes are allowed."

    # Maximum size (5 MB)
    if uploaded_file.size > 5 * 1024 * 1024:

        return False, "Resume size should be less than 5 MB."

    # Check PDF signature
    uploaded_file.seek(0)

    header = uploaded_file.read(4)

    uploaded_file.seek(0)

    if header != b"%PDF":

        return False, "Invalid PDF file."

    return True, ""


def validate_resume_text(text):

    if not text.strip():

        return (
            False,
            "No readable text found in the uploaded PDF."
        )

    if len(text.strip()) < 150:

        return (
            False,
            "Resume contains very little text."
        )

    return (
        True,
        ""
    )

def generate_resume_hash(text):

    return hashlib.sha256(

        text.encode()

    ).hexdigest()

def generate_resume_hash(text):
    """
    Generate a unique SHA-256 hash for resume text.
    """

    return hashlib.sha256(
        text.strip().encode("utf-8")
    ).hexdigest()