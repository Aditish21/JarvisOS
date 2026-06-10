from agents.router import route_query

from core.local_llm import ask_ai
from rag.rag_chat import ask_pdf


def run_agent(query):

    route = route_query(query)

    print(f"\n[ROUTE] {route}")

    if route == "pdf":
        return ask_pdf(query)

    return ask_ai(query)