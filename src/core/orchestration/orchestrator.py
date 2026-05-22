"""Main orchestrator for agent coordination"""

from typing import Dict, Any, List
from ..agents.base_agent import BaseAgent, Message


class Orchestrator:
    """Coordinates execution across all agents"""

    def __init__(self):
        """Initialize orchestrator"""
        self.agents: Dict[str, BaseAgent] = {}
        self.execution_history: List[Message] = []

    def register_agent(self, agent: BaseAgent) -> None:
        """Register an agent with the orchestrator.
        
        Args:
            agent: Agent to register
        """
        self.agents[agent.agent_id] = agent

    async def route_message(self, message: Message) -> Message:
        """Route a message to the appropriate agent.
        
        Args:
            message: Message to route
            
        Returns:
            Response from the target agent
        """
        if message.target_agent not in self.agents:
            raise ValueError(f"Agent {message.target_agent} not found")
        
        agent = self.agents[message.target_agent]
        response = await agent.handle_message(message)
        self.execution_history.append(message)
        
        return response

    def get_agent_status(self, agent_id: str) -> Dict[str, Any]:
        """Get status of a specific agent.
        
        Args:
            agent_id: Agent identifier
            
        Returns:
            Agent status information
        """
        if agent_id not in self.agents:
            return {"status": "not_found"}
        
        agent = self.agents[agent_id]
        return agent.get_metadata()

    def get_all_agents_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all registered agents.
        
        Returns:
            Dictionary of agent statuses
        """
        return {agent_id: agent.get_metadata() for agent_id, agent in self.agents.items()}
