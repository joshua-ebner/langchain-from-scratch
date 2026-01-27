# Document Loading and Splitting

This section demonstrates how **external data sources are ingested into LangChain**
and converted into a common internal representation: `Document` objects — and how
those documents are **split into chunks** suitable for downstream processing.

Document loading and splitting together form the **ingestion layer** of an LLM system.

---

## What is a Document?

In LangChain, a `Document` consists of:

- **`page_content`** — the raw text extracted from a source
- **`metadata`** — information about where the text came from (file, URL, page number, etc.)

All downstream operations (splitting, embedding, retrieval) operate on `Document` objects.

---

## Document Loading

The `loading/` folder demonstrates how different external data sources are converted
into LangChain `Document` objects.

### Loaders demonstrated

#### 1. Local text files

`loading/text_loader_basic.py` shows how to load a plain text file into one or more
`Document` objects.

Use case:
- internal notes
- reports
- logs
- exported text data

---

#### 2. Web pages

`loading/web_loader_basic.py` demonstrates loading a web page and extracting visible
text from HTML.

Use case:
- public documentation
- knowledge bases
- articles
- reference material

The output is intentionally **raw and unfiltered**. Cleaning and chunking happen later.

---

#### 3. PDF documents

`loading/pdf_loader_basic.py` shows how to load a multi-page PDF and convert each page
into a separate `Document`.

Use case:
- earnings reports
- strategy decks
- whitepapers
- regulatory filings

Each page becomes an independent unit with rich metadata (page number, source, author).

---

## Document Splitting (Chunking)

Once documents are loaded, they are typically **split into smaller chunks** before
being embedded or retrieved.

Splitting is necessary because:
- LLMs have finite context windows
- retrieval operates at the chunk level, not the full document
- smaller chunks improve relevance and reduce noise

There is no single “correct” chunking strategy — it is a tradeoff between **structure,
context, and size**.

The `splitting/` folder demonstrates two common approaches.

---

### Recursive text splitting

Files:
- `splitting/recursive_text_splitter_basic.py`
- `splitting/recursive_text_splitter_code.py`

The `RecursiveCharacterTextSplitter` is a **general-purpose splitter** that attempts
to preserve semantic coherence by splitting along natural boundaries in order:
paragraphs → sentences → words → characters.

Use case:
- plain text
- PDFs
- long-form prose
- mixed or unstructured content

This is often the default choice when document structure is weak or inconsistent.

---

### Markdown-aware splitting

File:
- `splitting/markdown_splitter_basic.py`

The `MarkdownTextSplitter` is **structure-aware** and prefers splitting at:
- section headers
- Markdown boundaries
- formatting cues

Use case:
- technical documentation
- strategy memos
- design docs
- README-style content

Because chunk overlap is enabled, content from adjacent sections may appear together.
This is expected and helps preserve context across boundaries.

---

### Chunk overlap and context preservation

All splitters support **chunk overlap**, which intentionally duplicates a small amount
of text between chunks.

Overlap exists to:
- preserve context across boundaries
- avoid cutting ideas in half
- improve downstream retrieval quality

Overlap is a tradeoff, not a bug.

---

## Key idea

At the ingestion stage, the goal is **faithful transformation**, not optimization.

- Load all potentially relevant text
- Preserve source metadata
- Split documents in a way that balances structure and context

Embedding, retrieval, and RAG strategies build on top of this foundation.
