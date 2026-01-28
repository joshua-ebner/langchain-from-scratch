# 10_RAG

This folder demonstrates basic Retrieval-Augmented Generation (RAG) patterns.

RAG combines retrieval with language model generation by first selecting relevant information and then using it as context for an LLM response.

The goal here is to make the RAG data flow explicit and easy to inspect.

## What is demonstrated

### Naive RAG

The simplest possible RAG loop:

- Store text as embeddings in a vector store
- Retrieve the most relevant text for a user query
- Inject the retrieved text into a prompt
- Generate an answer using an LLM

This version is intentionally minimal:
- One retrieval step
- Plain text context
- No re-ranking
- No agents
- No memory

The focus is on understanding how retrieval influences generation.

### Structured RAG

Structured RAG uses the same retrieval mechanism but changes how retrieved text is presented to the model.

Instead of mixing instructions, context, and the question together, the prompt explicitly separates them.

This makes it clear to the model:
- what information is grounding context
- what the task is
- what it should and should not rely on

Structured RAG typically produces answers that are:
- more conservative
- more grounded
- less prone to hallucination

The goal is not better retrieval, but better use of retrieved information.

## Why this matters

RAG is not about prompting tricks.  
It is about controlling what information the model is allowed to see and how it interprets that information.

Retrieval selects the candidate information.  
Prompt structure determines whether the model actually uses it.

## Mental model

- Embeddings define a semantic space
- Vector stores hold embedded text
- Retrieval selects which text becomes context
- Prompt structure controls how the model treats that context
- The language model generates an answer based on the provided context

If retrieval is wrong, generation will be wrong.  
If prompt structure is weak, retrieval may be ignored.

## Next steps

Later patterns build on this foundation by:
- analyzing RAG failure modes
- introducing agent-driven retrieval
- combining retrieval with tools and control loops
