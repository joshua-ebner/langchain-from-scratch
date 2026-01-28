"""
embedding_metadata.py

Purpose:
--------
Demonstrate that embeddings operate ONLY on text content and
completely ignore metadata.

Two inputs with identical text but different metadata will produce
identical embeddings.
"""

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings

# ------------------------------------------------------------------
# Example "documents"
# ------------------------------------------------------------------
# These mimic what you would normally get AFTER loading/splitting:
# text + metadata.
text = "Embeddings capture semantic meaning, not metadata."

doc_a = {
    "text": text,
    "metadata": {"source": "dummy_filename_a.txt", "page": 1},
}

doc_b = {
    "text": text,
    "metadata": {"source": "dummy_filename_b.txt", "page": 99},
}

# ------------------------------------------------------------------
# Initialize embedding model
# ------------------------------------------------------------------
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# ------------------------------------------------------------------
# Embed ONLY the text
# ------------------------------------------------------------------
vector_a = embeddings.embed_query(doc_a["text"])
vector_b = embeddings.embed_query(doc_b["text"])

# ------------------------------------------------------------------
# Compare results
# – Same embedded text, different metadata
# ------------------------------------------------------------------
same = vector_a == vector_b

print("Text A == Text B:", doc_a["text"] == doc_b["text"])
print("Metadata A:", doc_a["metadata"])
print("Metadata B:", doc_b["metadata"])
print()

print("Embedding dimensions:", len(vector_a))
print("Embeddings identical:", same)
print()

print("First 5 values (A):", vector_a[:5])
print("First 5 values (B):", vector_b[:5])
