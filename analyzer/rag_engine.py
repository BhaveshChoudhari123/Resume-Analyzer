from sentence_transformers import SentenceTransformer

from .pipelines.chunk_pipeline import create_chunks
from .pipelines.embedding_pipeline import generate_embeddings
from .pipelines.vector_pipeline import create_vector_store
from .pipelines.retrieval_pipeline import retrieve_chunks
from .pipelines.rag_pipeline import generate_answer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def process_resume(text):

    chunks = create_chunks(
        text
    )

    embeddings = generate_embeddings(
        chunks
    )

    index = create_vector_store(
        embeddings
    )

    return chunks, index


def ask_resume_question(
    question,
    chunks,
    index
):

    relevant_chunks = retrieve_chunks(
        question,
        chunks,
        index,
        model
    )

    context = "\n\n".join(
        relevant_chunks
    )

    answer = generate_answer(
        question,
        context
    )

    return answer