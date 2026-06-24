from groq import Groq
import os


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def improve_resume(resume_text):

    prompt = f"""
Analyze this resume and provide:

1. Missing skills
2. Missing technologies
3. Resume improvements
4. Career suggestions

Resume:

{resume_text}
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content