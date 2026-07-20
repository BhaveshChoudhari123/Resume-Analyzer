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


def generate_embeddings(chunks):

    model = get_model()

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        batch_size=4,
        show_progress_bar=False,
        normalize_embeddings=True
    )

    return embeddings