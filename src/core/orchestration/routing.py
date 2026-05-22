"""Message routing system"""

from typing import Dict, Any, Callable, Awaitable


class Router:
    """Handles routing of messages between agents"""

    def __init__(self):
        """Initialize router"""
        self.routes: Dict[str, Dict[str, Callable]] = {}
        self.middleware: list = []

    def register_route(
        self,
        source_agent: str,
        target_agent: str,
        handler: Callable,
    ) -> None:
        """Register a route between agents.
        
        Args:
            source_agent: Source agent ID
            target_agent: Target agent ID
            handler: Handler function
        """
        if source_agent not in self.routes:
            self.routes[source_agent] = {}
        self.routes[source_agent][target_agent] = handler

    def add_middleware(self, middleware: Callable) -> None:
        """Add middleware to process all messages.
        
        Args:
            middleware: Middleware function
        """
        self.middleware.append(middleware)
