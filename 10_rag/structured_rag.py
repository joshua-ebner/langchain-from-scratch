"""
structured_rag.py

Purpose
-------
Demonstrate a structured RAG pattern where retrieved context
is explicitly separated from instructions and the user question.

This reduces ambiguity about:
- what is grounding context
- what is the task
- what the model is allowed to use

Goal
----
Show how prompt structure affects RAG behavior.
"""

from typing import List
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from primitives.vector_stores.in_memory_vector_store import InMemoryVectorStore


# ---------------------------------------------------------------------
# Setup helpers
# ---------------------------------------------------------------------
def build_store(embeddings: OpenAIEmbeddings) -> InMemoryVectorStore:
    store = InMemoryVectorStore()

    texts = [
        "Embeddings map text into high-dimensional vector space.",
        "Vector stores enable similarity-based retrieval.",
        "Retrieval selects which context is passed to the language model.",
        "Paris is the capital of France.",
        "RAG combines retrieval with generation.",
    ]

    for i, text in enumerate(texts):
        vec = embeddings.embed_query(text)
        store.add(vec, {"id": i + 1, "text": text}) #index at 1 for human readability

    return store


def retrieve_context(
    store: InMemoryVectorStore,
    embeddings: OpenAIEmbeddings,
    query: str,
    k: int = 3
) -> List[str]:
    query_vec = embeddings.embed_query(query)
    results = store.similarity_search(query_vec, k=k)
    return [meta["text"] for _, meta in results]


# ---------------------------------------------------------------------
# Structured RAG
# ---------------------------------------------------------------------
def structured_rag(
    llm: ChatOpenAI,
    context_chunks: List[str],
    question: str
) -> str:
    """
    Generate an answer using explicitly structured context.
    """
    formatted_context = "\n".join(
        f"- {chunk}" for chunk in context_chunks
    )

    prompt = f"""
You are answering a question using ONLY the information in the context below.

Context:
{formatted_context}

Question:
{question}

Answer:
""".strip()

    response = llm.invoke(prompt)
    return response.content


# ---------------------------------------------------------------------
# Run demo
# ---------------------------------------------------------------------
if __name__ == "__main__":
    load_dotenv()

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    store = build_store(embeddings)

    question = "What role do vector stores play in RAG systems?"
    context = retrieve_context(store, embeddings, question, k=3)
    answer = structured_rag(llm, context, question)

    print("Question:")
    print(question)

    print("\nRetrieved context:")
    for c in context:
        print("-", c)

    print("\nAnswer:")
    print(answer)
