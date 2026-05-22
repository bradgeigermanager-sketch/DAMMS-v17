"""Base class for layers"""

from typing import Dict, Any, List
from ..core.agents.base_agent import BaseAgent


class LayerBase:
    """Base class for system layers"""

    def __init__(self, layer_id: str, layer_name: str, layer_order: int):
        """Initialize a layer.
        
        Args:
            layer_id: Unique layer identifier
            layer_name: Human-readable layer name
            layer_order: Position in layer hierarchy
        """
        self.layer_id = layer_id
        self.layer_name = layer_name
        self.layer_order = layer_order
        self.agents: Dict[str, BaseAgent] = {}

    def register_agent(self, agent: BaseAgent) -> None:
        """Register an agent in this layer.
        
        Args:
            agent: Agent to register
        """
        self.agents[agent.agent_id] = agent

    def get_layer_metadata(self) -> Dict[str, Any]:
        """Get metadata about this layer.
        
        Returns:
            Layer metadata
        """
        return {
            "layer_id": self.layer_id,
            "layer_name": self.layer_name,
            "layer_order": self.layer_order,
            "agent_count": len(self.agents),
            "agents": list(self.agents.keys()),
        }
