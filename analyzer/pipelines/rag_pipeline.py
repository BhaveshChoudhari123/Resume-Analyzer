from dotenv import load_dotenv
import os

load_dotenv()

from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(
    question,
    context
):

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {
                "role": "system",
                "content":
                """
                You are an AI Resume Assistant.

                Answer only from the provided resume context.

                If information is unavailable, reply:

                'This information is not present in the uploaded resume.'
                """
            },

            {
                "role": "user",
                "content":
                f"""
                Resume Context:

                {context}

                Question:

                {question}
                """
            }

        ],

        temperature=0.2,
        max_tokens=300
    )

    return response.choices[0].message.content