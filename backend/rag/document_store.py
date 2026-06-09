import chromadb
import uuid

from memory.embedding import create_embedding

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def save_chunks(chunks):

    for chunk in chunks:

        embedding = create_embedding(
            chunk
        )

        collection.add(
            ids=[str(uuid.uuid4())],
            embeddings=[embedding],
            documents=[chunk]
        )