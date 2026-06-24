import numpy as np


def retrieve_chunks(
    question,
    chunks,
    index,
    model
):

    question_embedding = model.encode(
        [question]
    )

    distances, indices = index.search(
        np.array(
            question_embedding,
            dtype="float32"
        ),
        k=2
    )

    results = []

    for i in indices[0]:

        results.append(
            chunks[i]
        )

    return results