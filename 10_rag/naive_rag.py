"""
naive_rag.py

Purpose
-------
Demonstrate the simplest possible Retrieval-Augmented Generation (RAG) loop:

1. Embed and store text
2. Retrieve relevant text for a query
3. Inject retrieved text into a prompt
4. Call the LLM to generate an answer

This is intentionally "naive":
- single retrieval step
- plain text context injection
- no agents
- no re-ranking
- no memory

Goal
----
Make the RAG data flow obvious and concrete.
"""

from typing import List
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from primitives.vector_stores.in_memory_vector_store import InMemoryVectorStore


# ---------------------------------------------------------------------
# Setup helpers
# ---------------------------------------------------------------------
def build_store(embeddings: OpenAIEmbeddings) -> InMemoryVectorStore:
    """Create a tiny demo vector store."""
    store = InMemoryVectorStore()

    texts = [
        "Embeddings map text into high-dimensional vector space.",
        "Vector stores enable similarity-based retrieval.",
        "Retrieval selects which context is passed to the language model.",
        "Paris is the capital of France.",
        "RAG combines retrieval with generation."
    ]

    for i, text in enumerate(texts):
        vec = embeddings.embed_query(text)
        store.add(vec, {"id": i + 1, "text": text})

    return store


def retrieve_context(
    store: InMemoryVectorStore,
    embeddings: OpenAIEmbeddings,
    query: str,
    k: int = 3
) -> List[str]:
    """Retrieve top-k relevant text chunks."""
    query_vec = embeddings.embed_query(query)
    results = store.similarity_search(query_vec, k=k)
    return [meta["text"] for _, meta in results]


# ---------------------------------------------------------------------
# Naive RAG
# ---------------------------------------------------------------------
def naive_rag(
    llm: ChatOpenAI,
    context_chunks: List[str],
    question: str
) -> str:
    """Generate an answer using retrieved context."""
    context = "\n".join(context_chunks)

    prompt = f"""
            Use the context below to answer the question.
            
            Context:
            {context}
            
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

    question = "How do vector stores help RAG systems?"
    context = retrieve_context(store, embeddings, question, k=3)
    answer = naive_rag(llm, context, question)

    print("Question:")
    print(question)
    print("\nRetrieved context:")
    for c in context:
        print("-", c)
    print("\nAnswer:")
    print(answer)
