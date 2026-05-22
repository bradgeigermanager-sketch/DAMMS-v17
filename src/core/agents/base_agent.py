"""Base agent class for all DAMMS agents"""

from enum import Enum
from typing import Dict, Any, Optional, Callable, Awaitable
from dataclasses import dataclass, field
from uuid import uuid4
import asyncio
from datetime import datetime


class AgentRole(str, Enum):
    """Enumeration of agent roles"""
    ORCHESTRATOR = "orchestrator"
    MANAGER = "manager"
    SPECIALIST = "specialist"
    VALIDATOR = "validator"
    INFRASTRUCTURE = "infrastructure"


@dataclass
class AgentCapability:
    """Represents a capability an agent can perform"""
    name: str
    description: str
    requires: list = field(default_factory=list)
    produces: list = field(default_factory=list)


@dataclass
class Message:
    """Standard message format for inter-agent communication"""
    id: str = field(default_factory=lambda: str(uuid4()))
    source_agent: str = ""
    target_agent: str = ""
    message_type: str = ""
    content: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    trace_id: str = field(default_factory=lambda: str(uuid4()))
    parent_trace_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class BaseAgent:
    """Base class for all DAMMS agents"""

    def __init__(
        self,
        agent_id: str,
        role: AgentRole,
        domain: str = "",
        description: str = "",
    ):
        """Initialize a base agent.
        
        Args:
            agent_id: Unique identifier for this agent
            role: Role of the agent in the system
            domain: Domain or specialization of the agent
            description: Human-readable description
        """
        self.agent_id = agent_id
        self.role = role
        self.domain = domain
        self.description = description
        self.capabilities: Dict[str, AgentCapability] = {}
        self.dependencies: list = []
        self.is_active = True
        self.message_queue: asyncio.Queue = asyncio.Queue()

    def add_capability(self, capability: AgentCapability) -> None:
        """Add a capability to this agent.
        
        Args:
            capability: Capability to add
        """
        self.capabilities[capability.name] = capability

    def add_dependency(self, agent_id: str) -> None:
        """Add a dependency on another agent.
        
        Args:
            agent_id: ID of the dependency agent
        """
        if agent_id not in self.dependencies:
            self.dependencies.append(agent_id)

    async def handle_message(self, message: Message) -> Message:
        """Process an incoming message.
        
        Args:
            message: Message to process
            
        Returns:
            Response message
        """
        raise NotImplementedError("Agents must implement handle_message")

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a task.
        
        Args:
            task: Task specification
            
        Returns:
            Task result
        """
        raise NotImplementedError("Agents must implement execute")

    def validate_inputs(self, inputs: Dict[str, Any]) -> bool:
        """Validate that inputs meet requirements.
        
        Args:
            inputs: Input dictionary to validate
            
        Returns:
            True if valid, False otherwise
        """
        return True

    def get_metadata(self) -> Dict[str, Any]:
        """Get metadata about this agent.
        
        Returns:
            Agent metadata
        """
        return {
            "agent_id": self.agent_id,
            "role": self.role.value,
            "domain": self.domain,
            "description": self.description,
            "capabilities": list(self.capabilities.keys()),
            "dependencies": self.dependencies,
            "is_active": self.is_active,
        }
