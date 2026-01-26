# Document Loading

This section demonstrates how **external data sources are ingested into LangChain**
and converted into a common internal representation: `Document` objects.

Document loading is the first boundary between the outside world and an LLM system.

---

## What is a Document?

In LangChain, a `Document` consists of:

- **`page_content`** — the raw text extracted from a source
- **`metadata`** — information about where the text came from (file, URL, page number, etc.)

All downstream operations (splitting, embedding, retrieval) operate on `Document` objects.

---

## Loaders demonstrated

This section includes three common loading patterns:

### 1. Local text files

`loading/text_loader_basic.py` shows how to load a plain text file into one or more
`Document` objects.

Use case:
- internal notes
- reports
- logs
- exported text data

---

### 2. Web pages

`loading/web_loader_basic.py` demonstrates loading a web page and extracting visible
text from HTML.

Use case:
- public documentation
- knowledge bases
- articles
- reference material

The output is intentionally **raw and unfiltered**. Cleaning and chunking happen later.

---

### 3. PDF documents

`loading/pdf_loader_basic.py` shows how to load a multi-page PDF and convert each page
into a separate `Document`.

Use case:
- earnings reports
- strategy decks
- whitepapers
- regulatory filings

Each page becomes an independent unit with rich metadata (page number, source, author).

---

## Key idea

At the loading stage, the goal is **completeness, not cleanliness**.

- Load all potentially relevant text
- Preserve source metadata
- Avoid premature filtering or chunking

Splitting, embedding, and retrieval are handled in later layers.

This section establishes a reliable, repeatable ingestion foundation.
