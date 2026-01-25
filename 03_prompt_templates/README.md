# Prompt Templates

This section introduces **prompt templates**, which allow you to structure
and reuse prompts with dynamic variables.

Two approaches are demonstrated:

– **PromptTemplate**  
  A string-based template where variables are interpolated into a single prompt.
  Useful for simple, text-only prompting.

– **ChatPromptTemplate**  
  A role-aware template that explicitly defines system and human messages.
  Useful when message roles and conversational structure matter.

In both cases, the key idea is the same:
**separate prompt structure from prompt inputs**, while keeping execution
explicit and transparent.