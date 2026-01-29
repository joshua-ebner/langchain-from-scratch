"""
tool_basics.py

Purpose
-------
Define the actions an agent can take.

Tools are:
- explicit
- side-effectful
- callable by the LLM

They do NOT decide *when* to run.
They only define *what is possible*.
"""

from langchain.tools import tool


@tool
def echo(text: str) -> str:
    """
    Echo the input text back verbatim.
    Useful for testing tool invocation.
    """
    return text


@tool
def add(a: int, b: int) -> int:
    """
    Add two integers.
    Simple deterministic tool.
    """
    return a + b


@tool
def search_notes(query: str) -> str:
    """
    Fake search tool.

    Pretend this queries a knowledge base.
    """
    notes = {
        "rag": "RAG combines retrieval with generation.",
        "vector store": "Vector stores enable similarity-based retrieval.",
        "agent": "Agents decide actions using a control loop."
    }

    for key, value in notes.items():
        if key in query.lower():
            return value

    return "No relevant notes found."
