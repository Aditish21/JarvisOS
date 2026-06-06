from memory.embedding import create_embedding
vector = create_embedding(
    "I love Python"
)
print(vector[:10])