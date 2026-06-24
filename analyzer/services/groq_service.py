from groq import Groq
import os


def get_groq_client():

    return Groq(
        api_key=os.getenv(
            "GROQ_API_KEY"
        )
    )