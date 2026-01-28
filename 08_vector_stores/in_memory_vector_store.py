"""
in_memory_vector_store.py

Purpose
-------
Demonstrate what a vector store *is*, at its core:

- store embedding vectors
- associate metadata
- perform similarity search
- return ranked results

This implementation is intentionally:
- in-memory only
- simple
- explicit

No persistence.
No indexing tricks.
No LangChain abstractions.

Goal
----
Make the vector-store concept concrete and inspectable.
"""

from typing import List, Dict, Any, Tuple
import numpy as np


class InMemoryVectorStore:
    def __init__(self):
        # Two parallel lists, where vectors[i] corresponds to metadata[i]
        self._vectors: List[np.ndarray] = []
        self._metadata: List[Dict[str, Any]] = []

    def add(
        self,
        vector: List[float],
        metadata: Dict[str, Any]
    ) -> None:
        """
        Store a single embedding vector with associated metadata.
        """
        self._vectors.append(np.array(vector))
        self._metadata.append(metadata)

    def similarity_search(
        self,
        query_vector: List[float],
        k: int = 3
    ) -> List[Tuple[float, Dict[str, Any]]]:
        """
        Perform cosine similarity search.

        Returns:
            List of (similarity_score, metadata), sorted descending.
        """
        if not self._vectors:
            return []

        query = np.array(query_vector)

        similarities = []
        for vec, meta in zip(self._vectors, self._metadata):
            score = self._cosine_similarity(query, vec)
            similarities.append((score, meta))

        # Sort by similarity descending
        similarities.sort(key=lambda x: x[0], reverse=True)

        return similarities[:k]

    @staticmethod
    def _cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
        """
        Compute cosine similarity between two vectors.
        """
        return float(
            np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        )


# ---------------------------------------------------------------------
# Example usage (optional, can be deleted later)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    from dotenv import load_dotenv
    from langchain_openai import OpenAIEmbeddings

    load_dotenv()
    
    store = InMemoryVectorStore()
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    v1 = embeddings.embed_query("Embeddings map text to vectors")
    v2 = embeddings.embed_query("Vector stores enable semantic search")
    v3 = embeddings.embed_query("Paris is the capital of France")

    store.add(v1, {"id": 1, "text": "Embeddings map text to vectors"})
    store.add(v2, {"id": 2, "text": "Vector stores enable semantic search"})
    store.add(v3, {"id": 3, "text": "Paris is the capital of France"})

    results = store.similarity_search(v1, k=2) # get top 2 results

    for score, meta in results:
        print(round(score, 4), meta)
