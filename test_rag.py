from analyzer.rag_engine import (
    split_resume,
    create_vector_store,
    ask_resume_question
)

text = """
Python Django HTML CSS MySQL

Projects:
AI Resume Analyzer
Cricketer Performance Tracker

Education:
BBA CA
"""

chunks = split_resume(text)

index = create_vector_store(
    chunks
)

answer = ask_resume_question(
    "What projects have I built?",
    chunks,
    index
)

print(answer)