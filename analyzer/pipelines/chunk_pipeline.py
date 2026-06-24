from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )

    return splitter.split_text(text)