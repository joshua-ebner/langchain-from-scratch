"""
Basic example: splitting Markdown documents using MarkdownTextSplitter.

Demonstrates:
- preserving section boundaries (headers)
- why Markdown-aware splitting matters
- how structured metadata is retained
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownTextSplitter


# ---------------------------------------------------------------------
# Load a Markdown document
# ---------------------------------------------------------------------

loader = TextLoader(
    file_path="example_markdown.md",
    encoding="utf-8",
)

documents = loader.load()

print(f"Original documents: {len(documents)}")


# ---------------------------------------------------------------------
# Define a Markdown-aware text splitter
# ---------------------------------------------------------------------

text_splitter = MarkdownTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

split_documents = text_splitter.split_documents(documents)

print(f"Number of Markdown chunks created: {len(split_documents)}\n")


# ---------------------------------------------------------------------
# Inspect a sample chunk
# ---------------------------------------------------------------------

sample_chunk = split_documents[-2]

print("Sample Markdown chunk:\n")
print(sample_chunk.page_content)

print("\nSample chunk metadata:\n")
print(sample_chunk.metadata)
