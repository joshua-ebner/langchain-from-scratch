"""
basic_vector_retrieval.py

Purpose
-------
Show the retrieval layer as a simple policy:

    query text -> embed -> similarity search -> ranked results

This intentionally avoids:
- RAG (no LLM call)
- chunking/loaders
- LangChain retriever abstractions
- vector DBs / indexes

It builds directly on the in-memory vector store from 08_vector_stores.
"""

from __future__ import annotations

from typing import Dict, Any, List, Tuple

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Import your primitive vector store implementation
from primitives.vector_stores.in_memory_vector_store import InMemoryVectorStore



def embed_text(embeddings: OpenAIEmbeddings, text: str) -> List[float]:
    """Embed a single string into a vector."""
    return embeddings.embed_query(text)


def build_demo_store(embeddings: OpenAIEmbeddings) -> InMemoryVectorStore:
    """
    Build a tiny store to make retrieval behavior obvious.

    Notes:
    - We embed each text (pretend these are already "chunks")
    - Metadata holds the text so we can inspect retrieval results
    """
    store = InMemoryVectorStore()

    items: List[Dict[str, Any]] = [
        {"id": 1, "text": "Embeddings map text to vectors."},
        {"id": 2, "text": "Vector stores enable semantic similarity search."},
        {"id": 3, "text": "Retrieval is a policy: decide what context to fetch."},
        {"id": 4, "text": "The Eiffel Tower is in Paris."},
        {"id": 5, "text": "Cosine similarity compares vectors by angle."},
    ]

    for item in items:
        vec = embed_text(embeddings, item["text"])
        store.add(vec, item)

    return store


def retrieve(
    store: InMemoryVectorStore,
    embeddings: OpenAIEmbeddings,
    query: str,
    k: int = 3,
) -> List[Tuple[float, Dict[str, Any]]]:
    """
    Retrieval policy:
    - embed query
    - similarity search over stored vectors
    - return top-k (score, metadata)
    """
    query_vec = embed_text(embeddings, query)
    return store.similarity_search(query_vec, k=k)


if __name__ == "__main__":
    load_dotenv()

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    store = build_demo_store(embeddings)

    query = "How do vector stores help with semantic search?"
    results = retrieve(store, embeddings, query=query, k=10)

    print("Query:", query)
    print("Top-k results:")
    for score, meta in results:
        print(f"  score={score:.4f}  id={meta.get('id')}  text={meta.get('text')}")
