"""
basic_embedding.py

Absolute-minimum embeddings demo:
- embed a single string
- print dimensionality
- print a small prefix of the vector
"""

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text = "LangChain provides abstractions for building LLM-powered systems."

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector = embeddings.embed_query(text)

print("embedding_dim:", len(vector))
print("sample_values:", vector[:10])
