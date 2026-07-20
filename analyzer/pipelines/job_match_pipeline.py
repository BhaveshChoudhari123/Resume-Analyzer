import numpy as np

MODEL = None


def get_model():
    global MODEL

    if MODEL is None:
        from sentence_transformers import SentenceTransformer

        MODEL = SentenceTransformer(
            "all-MiniLM-L6-v2",
            device="cpu"
        )

    return MODEL


def calculate_match_score(resume_text, job_description):

    model = get_model()

    embeddings = model.encode(
        [resume_text, job_description],
        convert_to_numpy=True,
        batch_size=2,
        show_progress_bar=False,
        normalize_embeddings=True
    )

    # Since embeddings are normalized,
    # dot product gives cosine similarity
    similarity = np.dot(
        embeddings[0],
        embeddings[1]
    )

    score = round(
        float(similarity) * 100,
        2
    )

    return score