# Basic Execution and Control

This section focuses on **how LangChain code actually runs**, before introducing
higher-level abstractions like chains, agents, or graphs.

The goal is to understand execution mechanics clearly and explicitly.

## What this section covers

### 1. Execution interfaces

`execution_interface_methods_basic.py` demonstrates the three primary ways
LangChain executes a model:

- **`invoke()`** — run a single prompt synchronously
- **`batch()`** — run multiple prompts in a single call
- **`stream()`** — consume model output incrementally as it is generated

These are different execution interfaces over the *same underlying model*.

---

### 2. Imperative control flow

`imperative_control_flow_basic.py` shows how to:

- compose prompts and models manually
- control execution explicitly using standard Python
- expose LangChain runnable methods via the `@chain` decorator

This example emphasizes **clarity over abstraction**, making execution order
and data flow obvious.

---

### 3. Output parsing utilities

`output_parser_csv_list.py` demonstrates a simple output parser that converts
comma-separated text into a structured Python list.

This illustrates how **lightweight parsing** can be layered on top of raw model
output without introducing full schemas or chains.

---

## Key idea

Before building complex systems, it’s critical to understand:

- how models are executed
- how results are returned
- how control flow is handled explicitly

This section establishes those fundamentals.
