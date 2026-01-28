"""
batch_embedding.py

Purpose:
--------
Demonstrate embedding multiple texts at once (batching) and
observe the structure of the returned result.

This file focuses on:
- one vector per input text
- preserved ordering
- consistent dimensionality

Intentionally avoids:
- metadata
- vector stores
- similarity math
"""

from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

texts = [
    "LangChain provides abstractions for LLM-powered systems.",
    "Embeddings map text into a high-dimensional vector space.",
    "Vector similarity enables semantic search and retrieval.",
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectors = embeddings.embed_documents(texts)

print("number_of_inputs:", len(texts))
print("number_of_vectors:", len(vectors))
print()

print("embedding_dim (first vector):", len(vectors[0]))
print()

for i, vector in enumerate(vectors):
    print(f"input_{i}_first_5_values:", vector[:5])
