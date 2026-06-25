from dotenv import load_dotenv
import os
import json
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)




def analyze_resume_with_ai(resume_text):

    prompt = f"""
Analyze this resume.

Return ONLY valid JSON.

Generate:

1. Resume Score
2. ATS Score
3. Resume Level
4. Resume Summary
5. Skills
6. Missing Skills
7. Recommended Jobs
8. Strengths
9. Weaknesses
10. Suggestions
11. 10 Interview Questions

Resume:

{resume_text[:4000]}

JSON:
{{
    "score": 0,
    "ats_score": 0,
    "resume_level": "",
    "resume_summary": "",
    "skills": [],
    "missing_skills": [],
    "recommended_jobs": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": [],
    "interview_questions": []
}}
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "Return only JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=1200
        )

        result = response.choices[0].message.content.strip()

        start = result.find("{")
        end = result.rfind("}")

        if start == -1 or end == -1:
            raise Exception("JSON not found")

        result = result[start:end + 1]

        data = json.loads(result)

        # AI Job Matcher
        skills = data.get("skills", [])

        job_match = []

        if "Python" in skills:
            job_match.append({
                "role": "Python Developer",
                "match": "92%"
            })

        if "Django" in skills:
            job_match.append({
                "role": "Backend Developer",
                "match": "88%"
            })

        if "MySQL" in skills:
            job_match.append({
                "role": "Database Developer",
                "match": "82%"
            })

        if "HTML" in skills or "CSS" in skills:
            job_match.append({
        "role": "Web Developer",
        "match": "80%"
    })

        if "Flask" in skills:
            job_match.append({
                "role": "Flask Developer",
                "match": "85%"
            })

        return {
            "score": data.get("score", 70),
            "ats_score": data.get("ats_score", 70),
            "resume_level": data.get("resume_level", "Good"),
            "resume_summary": data.get("resume_summary", ""),
            "skills": data.get("skills") or [],
            "missing_skills": data.get("missing_skills", []),
            "recommended_jobs": data.get("recommended_jobs", []),
            "strengths": data.get("strengths", []),
            "weaknesses": data.get("weaknesses", []),
            "suggestions": data.get("suggestions", []),
            "interview_questions": data.get("interview_questions",[]),
            "job_match": job_match,
        }

    except Exception as e:

        print("AI ERROR:", str(e))

        return {
            "score": 70,
            "ats_score": 70,
            "resume_level": "Good",
            "skills": [],
            "missing_skills": [],
            "recommended_jobs": [],
            "strengths": [
                "Resume uploaded successfully"
            ],
            "weaknesses": [
                "AI analysis failed"
            ],
            "suggestions": [
                "Check API key and try again"
            ],
            "job_match": []
        }