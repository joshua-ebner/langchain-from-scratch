"""
Basic example: splitting a loaded document into chunks using
RecursiveCharacterTextSplitter.

Demonstrates:
- why chunking is necessary
- how chunk size and overlap work
- what a split Document looks like
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ---------------------------------------------------------------------
# Load a document
# ---------------------------------------------------------------------

loader = TextLoader(
    file_path="example_long.txt",
    encoding="utf-8",
)

documents = loader.load()

print(f"Original documents: {len(documents)}")


# ---------------------------------------------------------------------
# Define a text splitter
# ---------------------------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,        # target size of each chunk (characters)
    chunk_overlap=50,      # overlap between chunks to preserve context
)

split_documents = text_splitter.split_documents(documents)

print(f"Number of chunks created: {len(split_documents)}\n")


# ---------------------------------------------------------------------
# Inspect a sample chunk
# ---------------------------------------------------------------------

sample_chunk = split_documents[0]

print("Sample chunk content:\n")
print(sample_chunk.page_content)

print("\nSample chunk metadata:\n")
print(sample_chunk.metadata)
