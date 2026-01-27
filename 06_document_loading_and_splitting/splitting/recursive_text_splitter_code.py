"""
Basic example: splitting source code using RecursiveCharacterTextSplitter.

Demonstrates:
- why code requires different chunking than prose
- how logical separators preserve structure
- how chunk size and overlap affect code integrity
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ---------------------------------------------------------------------
# Load a source code file
# ---------------------------------------------------------------------

loader = TextLoader(
    file_path="example_code.py",
    encoding="utf-8",
)

documents = loader.load()

print(f"Original documents: {len(documents)}")


# ---------------------------------------------------------------------
# Define a code-aware text splitter
# ---------------------------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=[
        "\nclass ",
        "\ndef ",
        "\n\n",
        "\n",
        " ",
        "",
    ],
)

split_documents = text_splitter.split_documents(documents)

print(f"Number of code chunks created: {len(split_documents)}\n")


# ---------------------------------------------------------------------
# Inspect a sample chunk
# ---------------------------------------------------------------------

sample_chunk = split_documents[-1]

print("Sample code chunk:\n")
print(sample_chunk.page_content)

print("\nSample chunk metadata:\n")
print(sample_chunk.metadata)
