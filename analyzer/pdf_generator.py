from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    response,
    score,
    ats_score,
    resume_level,
    skills,
    missing_skills,
    recommended_jobs,
    resume_summary,
    strengths,
    weaknesses,
    suggestions,
    interview_questions
):

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "AI Resume Analyzer Pro Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # Scores
    elements.append(
        Paragraph(
            f"Resume Score: {score}/100",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"ATS Score: {ats_score}/100",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Resume Level: {resume_level}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    # Skills
    elements.append(
        Paragraph(
            "Detected Skills",
            styles["Heading2"]
        )
    )

    for skill in skills:
        elements.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))

    # Missing Skills
    elements.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    for skill in missing_skills:
        elements.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))

    # Recommended Jobs
    elements.append(
        Paragraph(
            "Recommended Jobs",
            styles["Heading2"]
        )
    )

    for job in recommended_jobs:
        elements.append(
            Paragraph(
                f"• {job}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))

    # Resume Summary
    elements.append(
        Paragraph(
            "Resume Summary",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            str(resume_summary),
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 15))

    # Strengths
    elements.append(
        Paragraph(
            "Strengths",
            styles["Heading2"]
        )
    )

    for item in strengths:
        elements.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))

    # Weaknesses
    elements.append(
        Paragraph(
            "Weaknesses",
            styles["Heading2"]
        )
    )

    for item in weaknesses:
        elements.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))

    # Suggestions
    elements.append(
        Paragraph(
            "Suggestions",
            styles["Heading2"]
        )
    )

    for item in suggestions:
        elements.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 15))

    # Interview Questions
    elements.append(
        Paragraph(
            "Interview Questions",
            styles["Heading2"]
        )
    )

    for question in interview_questions:
        elements.append(
            Paragraph(
                f"• {question}",
                styles["Normal"]
            )
        )

    doc.build(elements)