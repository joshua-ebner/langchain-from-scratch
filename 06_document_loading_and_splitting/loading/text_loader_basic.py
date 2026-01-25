"""
Basic example: loading a local text file into LangChain Documents.

Demonstrates:
- using a TextLoader
- what a Document object contains (content + metadata)
"""

from langchain_community.document_loaders import TextLoader


# Load a local text file
loader = TextLoader(
    file_path="example.txt",
    encoding="utf-8",
)

documents = loader.load()


# Inspect the loaded documents
print(f"Number of documents loaded: {len(documents)}\n")

doc = documents[0]
print("Document content:\n")
print(doc.page_content)

print("\nDocument metadata:\n")
print(doc.metadata)
