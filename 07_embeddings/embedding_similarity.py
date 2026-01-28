"""
embedding_similarity.py

Purpose:
--------
Demonstrate how semantic similarity between texts is computed
using cosine similarity over embedding vectors.
"""

from langchain_openai import OpenAIEmbeddings
from langchain_community.utils.math import cosine_similarity

from dotenv import load_dotenv
load_dotenv()


texts = [
    "Embeddings map text into a high-dimensional vector space.",
    "Text embeddings represent semantic meaning as vectors.",
    "The capital of France is Paris.",
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectors = embeddings.embed_documents(texts)

vector_1, vector_2, vector_3 = vectors

sim_1_2 = cosine_similarity([vector_1], [vector_2])[0][0]
sim_1_3 = cosine_similarity([vector_1], [vector_3])[0][0]

print("Similarity (text 1 vs text 2):", round(sim_1_2, 4))
print("Similarity (text 1 vs text 3):", round(sim_1_3, 4))
