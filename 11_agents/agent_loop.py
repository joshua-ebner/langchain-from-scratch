"""
agent_loop.py

Purpose
-------
Demonstrate the core agent control loop explicitly.

This file shows:
- how agent state is read
- how a decision is made
- how tools are invoked
- how observations update state
- how the loop progresses step by step

Summary
-------
This is a minimal, LangChain-compatible agent loop built explicitly to show
how tools, state, and decisions interact.

No LangChain agent abstractions.
"""

from typing import Callable, Dict, Tuple, Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from primitives.agents.agent_state import AgentState
from primitives.agents.tool_basics import search_notes


# -----------------------------
# Tool registry
# -----------------------------
TOOLS: Dict[str, Callable[[str], str]] = {
    "search": search_notes,
}


# -----------------------------
# Decision step (THINK)
# -----------------------------
def decide_next_action(llm: ChatOpenAI, state: AgentState) -> str:
    """
    Ask the LLM what to do next based on current state.

    Returns a simple string command, e.g.:
    - "search: vector stores"
    - "finish"
    """
    prompt = f"""
You are a very simple agent.

You do NOT have access to any internal notes unless you use the search tool.
If the user asks about internal notes, you MUST search before answering.

Conversation so far:
{state.messages}

Observations so far:
{state.observations}

Decide ONE next action.

Rules:
- To use a tool, respond exactly: tool_name: query
- To stop, respond exactly: finish
"""
    response = llm.invoke(prompt)
    return response.content.strip()


# -----------------------------
# Termination check
# -----------------------------
def should_stop(action: str) -> bool:
    """Return True if the agent decided to stop."""
    return action == "finish"


# -----------------------------
# Action parsing
# -----------------------------
def parse_action(action: str) -> Optional[Tuple[str, str]]:
    """
    Parse an action string into (tool_name, tool_input).

    Returns None if the format is invalid.
    """
    if ":" not in action:
        return None

    tool_name, tool_input = action.split(":", 1)
    return tool_name.strip(), tool_input.strip()


# -----------------------------
# Tool execution (ACT)
# -----------------------------
def execute_tool(tool_name: str, tool_input: str) -> str:
    """
    Execute the named tool with the given input.

    Returns an observation string.
    """
    tool = TOOLS.get(tool_name)

    if tool is None:
        return f"Unknown tool: {tool_name}"

    return tool.invoke(tool_input)


# -----------------------------
# State update (OBSERVE)
# -----------------------------
def update_state(state: AgentState, action: str, observation: str) -> None:
    """
    Update agent state after an action is taken.
    """
    state.record_action(action)
    state.add_observation(observation)


# -----------------------------
# Agent loop
# -----------------------------
def run_agent(
    llm: ChatOpenAI,
    initial_question: str,
    max_steps: int = 5,
) -> AgentState:
    # Initialize agent state
    state = AgentState()
    state.add_message(initial_question)

    # Control loop: one iteration = one decision cycle
    for step in range(max_steps):
        print(f"\nStep {step + 1}")

        # THINK
        action = decide_next_action(llm, state)
        print("Action:", action)

        # STOP?
        if should_stop(action):
            print("Agent decided to stop.")
            break

        # ACT
        parsed = parse_action(action)
        if parsed is None:
            observation = "Invalid action format"
        else:
            tool_name, tool_input = parsed
            observation = execute_tool(tool_name, tool_input)

        # OBSERVE
        update_state(state, action, observation)
        print("Observation:", observation)

    return state


# -----------------------------
# Example run
# -----------------------------
if __name__ == "__main__":
    load_dotenv()

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    final_state = run_agent(
        llm,
        initial_question="What do my internal notes say about vector stores?",
    )

    print("\nFinal state:")
    print("Messages:", final_state.messages)
    print("Observations:", final_state.observations)
