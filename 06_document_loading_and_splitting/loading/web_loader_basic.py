"""
Basic example: loading a web page into LangChain Documents.

Demonstrates:
- using a WebBaseLoader
- converting HTML content into Document objects
- inspecting content and metadata
"""

from langchain_community.document_loaders import WebBaseLoader


# Load a single web page
loader = WebBaseLoader(
    "https://en.wikipedia.org/wiki/Contribution_margin"
)

documents = loader.load()


# Inspect the loaded documents
print(f"Number of documents loaded: {len(documents)}\n")

doc = documents[0]

print("Document content (truncated):\n")
print(doc.page_content[:1000])  # avoid dumping entire page

print("\nDocument metadata:\n")
print(doc.metadata)
