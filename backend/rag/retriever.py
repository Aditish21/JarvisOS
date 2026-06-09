from rag.document_store import collection
from memory.embedding import create_embedding


def retrieve_document(query):

    embedding = create_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    documents = results["documents"][0]

    return "\n".join(documents)