"""
agent_state.py

Purpose
-------
Define explicit state for an agent.

This makes agent behavior inspectable by tracking:
- interaction history
- last action taken
- observations from tool usage
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AgentState:
    messages: List[str] = field(default_factory=list)
    last_action: Optional[str] = None
    observations: List[str] = field(default_factory=list)

    def add_message(self, message: str) -> None:
        self.messages.append(message)

    def record_action(self, action: str) -> None:
        self.last_action = action

    def add_observation(self, observation: str) -> None:
        self.observations.append(observation)
