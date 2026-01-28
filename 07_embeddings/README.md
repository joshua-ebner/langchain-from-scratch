# 07_embeddings

This folder isolates the **embeddings layer** of an LLM system.

The goal is not to build retrieval, RAG, or agents.  
The goal is to understand—clearly and empirically—**what embeddings are, what they do, and what they do not do**.

At this layer, text stops being symbolic and becomes **geometric**.

---

## Mental model

An embedding model performs a single operation:

> **It projects a unit of text into a fixed-dimensional vector space.**

Key implications:

- Embeddings are numeric, not symbolic  
- Dimensionality is model-defined, not input-defined  
- Meaning is encoded as position in space  
- Structure and metadata do **not** survive embedding  

---

## Files in this folder

Each file demonstrates one specific property of embeddings, in isolation.

### `basic_embedding.py`

- One string → one vector  
- Fixed dimensionality (1536 for `text-embedding-3-small`)  
- Values are opaque floats  

**Takeaway:** an embedding is just a point in high-dimensional space.

---

### `batch_embedding.py`

- Multiple texts embedded in one call  
- One vector per input  
- Ordering preserved  
- Identical dimensionality across vectors  

**Takeaway:** batching is an efficiency concern, not a semantic one.

---

### `embedding_metadata.py`

- Same text, different metadata  
- Identical embeddings  

**Takeaway:** **metadata is not embedded** and must be handled outside the vector space.

---

### `embedding_similarity.py`

- Cosine similarity over embedding vectors  
- Related texts score high  
- Unrelated texts score near zero  

**Takeaway:** semantic similarity emerges as geometric proximity.

---

## Relationship to ingestion

In a full ingestion pipeline, the flow is:

- documents  
- split into chunks  
- each chunk embedded as a whole  
- one vector per chunk  

**Chunking defines semantic boundaries.**  
**Embedding only projects those boundaries into vector space.**

Once a chunk is embedded, the boundary is frozen and irreversible.

---

## What this layer excludes (by design)

- Vector stores  
- Persistence  
- Retrieval  
- RAG  
- Agents  
- Evaluation  

These belong in later layers.

---

## Key takeaways

- Embeddings are geometry, not language  
- Text length does not affect vector dimensionality  
- Metadata must be stored separately  
- Similarity is a numeric signal, not a truth  
- Ingestion decisions propagate downstream  
