import chromadb
from memory.embedding import create_embedding

# Fix 1: Persistent storage
client = chromadb.PersistentClient(path="./jarvis_memory_db")
collection = client.get_or_create_collection(
    name="jarvis_memory",
    metadata={"hnsw:space": "cosine"}  # cosine similarity for better matching
)

def save_memory(text, memory_id):
    embedding = create_embedding(text)
    collection.add(
        embeddings=[embedding],
        documents=[text],
        ids=[memory_id]
    )

def search_memory(query, threshold=0.4):
    embedding = create_embedding(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=3,  # get top 3, filter by threshold
        include=["documents", "distances"]
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    # Fix 3: Filter by similarity threshold
    filtered = [
        doc for doc, dist in zip(documents, distances)
        if dist < threshold  # lower distance = more similar in cosine
    ]

    return filtered