from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.document_store import save_chunks

text = load_pdf(
    "documents/sample.pdf"
)

chunks = chunk_text(text)

save_chunks(chunks)

print(
    f"{len(chunks)} chunks saved!"
)