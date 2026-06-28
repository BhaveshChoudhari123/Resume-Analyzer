from sentence_transformers import SentenceTransformer

MODEL = None


def get_model():
    global MODEL

    if MODEL is None:
        MODEL = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return MODEL


def generate_embeddings(chunks):

    model = get_model()

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        batch_size=8
    )

    return embeddings