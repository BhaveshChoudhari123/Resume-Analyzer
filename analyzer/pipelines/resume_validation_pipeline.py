import json
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def validate_resume_content(resume_text):

    prompt = f"""
You are an AI Document Classifier.

Your task is to identify whether the uploaded document is a professional Resume or CV.

Possible document types include:

- Resume
- CV
- Aadhaar Card
- PAN Card
- Passport
- Driving License
- Income Tax Return
- Invoice
- Bank Statement
- College Assignment
- Research Paper
- Certificate
- Offer Letter
- Any Other Document

Return ONLY valid JSON.

If the document is a Resume or CV:

{{
    "is_resume": true,
    "document_type": "Resume",
    "confidence": 98,
    "reason": "Professional resume detected."
}}

Otherwise:

{{
    "is_resume": false,
    "document_type": "<Detected Document>",
    "confidence": 97,
    "reason": "This document is not a professional resume."
}}

Document:

{resume_text[:4000]}
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {
                "role": "system",
                "content": "Return only valid JSON."
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0,

        max_tokens=300

    )

    result = response.choices[0].message.content

    start = result.find("{")
    end = result.rfind("}")

    result = result[start:end+1]

    return json.loads(result)