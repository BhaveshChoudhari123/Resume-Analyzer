import numpy as np


def retrieve_chunks(
    question,
    chunks,
    index,
    model
):

    question_embedding = model.encode(
        [question],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        question_embedding.astype("float32"),
        k=min(2, len(chunks))
    )

    results = []

    for i in indices[0]:
        if 0 <= i < len(chunks):
            results.append(chunks[i])

    return results