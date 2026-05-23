#!/usr/bin/env python3
"""Universal Coupling & Modular Data Routing Engine

Provides semantic telemetry fabric for routing and integrating data across DAMMS.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import json


class RoutingMode(Enum):
    """Data routing modes."""
    DIRECT = "direct"
    BROADCAST = "broadcast"
    HIERARCHICAL = "hierarchical"
    SEMANTIC = "semantic"


@dataclass
class TelemetryPacket:
    """Represents a telemetry data packet."""
    source: str
    destination: str
    data_type: str
    payload: Any
    routing_mode: RoutingMode
    metadata: Dict = field(default_factory=dict)
    semantic_tags: List[str] = field(default_factory=list)


class DataRoutingEngine:
    """Universal data routing and integration engine."""
    
    def __init__(self):
        self.routes: Dict[str, List[str]] = {}
        self.semantic_mappings: Dict[str, str] = {}
        self.packet_log: List[TelemetryPacket] = []
    
    def register_route(self, source: str, destinations: List[str]) -> None:
        """Register a routing path.
        
        Args:
            source: Source module/agent
            destinations: List of destination modules/agents
        """
        self.routes[source] = destinations
    
    def register_semantic_mapping(self, source_type: str, target_type: str) -> None:
        """Register a semantic type mapping.
        
        Args:
            source_type: Source data type
            target_type: Target data type
        """
        self.semantic_mappings[source_type] = target_type
    
    def route_packet(self, packet: TelemetryPacket) -> List[str]:
        """Route a telemetry packet to appropriate destinations.
        
        Args:
            packet: Telemetry packet to route
            
        Returns:
            List of actual destinations packet was routed to
        """
        destinations = []
        
        match packet.routing_mode:
            case RoutingMode.DIRECT:
                destinations = [packet.destination]
            
            case RoutingMode.BROADCAST:
                # Broadcast to all registered destinations
                destinations = self.routes.get(packet.source, [])
            
            case RoutingMode.HIERARCHICAL:
                # Route through hierarchy
                destinations = self._route_hierarchical(packet.source, packet.destination)
            
            case RoutingMode.SEMANTIC:
                # Route based on semantic tags and types
                destinations = self._route_semantic(packet)
        
        # Log packet
        self.packet_log.append(packet)
        
        return destinations
    
    def _route_hierarchical(self, source: str, destination: str) -> List[str]:
        """Route through hierarchical path."""
        # Simple hierarchical routing: follow registered routes
        if source in self.routes:
            return self.routes[source]
        return [destination]
    
    def _route_semantic(self, packet: TelemetryPacket) -> List[str]:
        """Route based on semantic analysis."""
        destinations = set()
        
        # Find destinations based on semantic tags
        for tag in packet.semantic_tags:
            if tag in self.semantic_mappings:
                mapped = self.semantic_mappings[tag]
                if mapped in self.routes:
                    destinations.update(self.routes[mapped])
        
        # Add direct destination if specified
        if packet.destination:
            destinations.add(packet.destination)
        
        return list(destinations)
    
    def integrate_data(self, packets: List[TelemetryPacket]) -> Dict[str, Any]:
        """Integrate multiple telemetry packets into unified data structure.
        
        Args:
            packets: List of packets to integrate
            
        Returns:
            Integrated data dictionary
        """
        integrated = {
            'sources': set(),
            'data_types': set(),
            'payloads': {},
            'metadata': {}
        }
        
        for packet in packets:
            integrated['sources'].add(packet.source)
            integrated['data_types'].add(packet.data_type)
            
            key = f"{packet.source}:{packet.data_type}"
            integrated['payloads'][key] = packet.payload
            integrated['metadata'][key] = packet.metadata
        
        # Convert sets to lists for JSON serialization
        integrated['sources'] = list(integrated['sources'])
        integrated['data_types'] = list(integrated['data_types'])
        
        return integrated


# Export engine
engine = DataRoutingEngine()
