import ollama

from rag.retriever import (
    retrieve_document
)


def ask_pdf(question):

    context = retrieve_document(
        question
    )

    messages = [
        {
            "role": "system",
            "content": f"""
Answer using ONLY the document context below.

DOCUMENT:

{context}

If the answer is not present,
say:
'I could not find that information in the document.'
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = ollama.chat(
        model="phi3:mini",
        messages=messages
    )

    return response["message"]["content"]