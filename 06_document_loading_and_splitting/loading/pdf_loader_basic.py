"""
Basic example: loading a PDF file into LangChain Documents.

Demonstrates:
- using a PDF loader
- extracting text from pages
- inspecting content and metadata
"""

from langchain_community.document_loaders import PyPDFLoader


# Load a local PDF file
loader = PyPDFLoader("example.pdf")

documents = loader.load()


# Inspect the loaded documents
print(f"Number of documents loaded: {len(documents)}\n")

doc = documents[0]

print("Document content (truncated):\n")
print(doc.page_content[:1000])  # avoid dumping entire PDF

print("\nDocument metadata:\n")
print(doc.metadata)
