from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text

text = load_pdf("documents/sample.pdf")

print("Text Length:", len(text))

chunks = chunk_text(text)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("Length:", len(chunk))