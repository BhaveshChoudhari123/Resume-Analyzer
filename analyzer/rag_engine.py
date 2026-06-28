from .pipelines.chunk_pipeline import create_chunks
from .pipelines.embedding_pipeline import (
    generate_embeddings,
    get_model
)
from .pipelines.vector_pipeline import create_vector_store
from .pipelines.retrieval_pipeline import retrieve_chunks
from .pipelines.rag_pipeline import generate_answer

VECTOR_CACHE = {}


def process_resume(text):

    if text in VECTOR_CACHE:
        return VECTOR_CACHE[text]

    chunks = create_chunks(text)

    embeddings = generate_embeddings(chunks)

    index = create_vector_store(embeddings)

    VECTOR_CACHE[text] = (chunks, index)

    return chunks, index


def ask_resume_question(
    question,
    chunks,
    index
):

    model = get_model()

    relevant_chunks = retrieve_chunks(
        question,
        chunks,
        index,
        model
    )

    context = "\n\n".join(relevant_chunks)

    answer = generate_answer(
        question,
        context
    )

    return answer