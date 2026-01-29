# 11_agents

This folder demonstrates the **core mechanics of an AI agent**, built explicitly and kept compatible with LangChain concepts—without relying on LangChain’s high-level agent abstractions.

The goal is to make agent behavior *visible and understandable*.

---

## What this shows

An agent is **not** a single prompt.

An agent is a loop:

1. **State** — what the agent knows so far
2. **Decision** — what to do next
3. **Action** — optionally call a tool
4. **Observation** — record what happened
5. **Repeat** — until the agent decides to stop

This folder implements that loop step by step.

---

## Files

### `agent_state.py`
Defines explicit agent state:
- messages (conversation history)
- last action
- observations from tools

State is stored and updated manually so behavior is inspectable.

---

### `tool_basics.py`
Defines the **actions the agent can take**.

Tools:
- are explicit
- are callable
- do not decide *when* to run
- only define *what is possible*

These are LangChain `@tool` functions, but invoked directly.

---

### `agent_loop.py`
Implements a **minimal LangChain-compatible agent loop**, explicitly.

Shows:
- how the LLM decides actions
- how tool calls are parsed
- how tools are executed
- how observations update state
- how the loop progresses over time

No hidden control flow.
Just: **THINK → ACT → OBSERVE → REPEAT**.

---

## Why this matters

High-level agent frameworks hide:
- when decisions are made
- how tools are chosen
- how state evolves
- why agents fail or loop

This code makes those mechanics concrete.

Once you understand this loop, LangChain agents stop being mysterious ... they’re just abstractions over the same pattern.

---

## What this is *not*

- Not a production agent
- Not optimized
- Not autonomous intelligence

This is a **learning artifact** designed to demonstrate agent system thinking clearly.

---

## Next directions

Possible extensions:
- multi-tool agents
- memory pruning
- planning vs reacting
- RAG-augmented agents
- failure modes and safeguards
