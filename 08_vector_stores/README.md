# 08_vector_stores

This folder isolates the **vector store layer** of an LLM system.

The purpose here is to make concrete what a vector store *is*, independent of
any database, framework, or production optimization.

---

## Mental model

A vector store answers one question:

> **Given a query vector, which stored vectors are most similar?**

At its core, a vector store does four things:

- stores embedding vectors
- associates each vector with metadata describing its source
- computes similarity between vectors
- returns ranked results

It does **not**:
- generate embeddings
- understand text
- decide *how* queries are formed
- perform reasoning

---

## Files in this folder

### `in_memory_vector_store.py`

A minimal, explicit implementation of a vector store using in-memory data
structures.

What it demonstrates:

- embedding vectors are stored
- metadata describing each vector’s source is stored separately
- each vector is associated with its metadata by index
- similarity search is pure geometry (cosine similarity)
- results are ranked and returned with metadata

Concretely, the association works as:

- `vectors[i]` and `metadata[i]` refer to the same stored item

This file intentionally avoids:
- persistence
- indexing (FAISS, HNSW, etc.)
- databases
- LangChain vector store abstractions

The goal is clarity, not scalability.

---

## Relationship to embeddings

Embedding happens **outside** the vector store.

The vector store is model-agnostic and assumes:
- all vectors live in the same embedding space
- semantic meaning has already been encoded upstream

This separation is intentional and fundamental.

---

## Why this layer exists

Understanding vector stores at this level makes it clear that:

- “memory” is just stored vectors plus metadata
- the store itself is semantically blind
- retrieval quality depends entirely on upstream embeddings
- higher-level systems (RAG, agents) are built on top of this primitive

---