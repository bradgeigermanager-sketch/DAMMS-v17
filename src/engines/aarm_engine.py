#!/usr/bin/env python3
"""Agnostic Agreement & Relationship Mapper (AARM) v2.0 Engine

Distributed legal-logic engine for computing net permissions across overlapping jurisdictions.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import json


class ConflictResolutionRule(Enum):
    """Hierarchy rules for conflict resolution."""
    LEX_SUPERIOR = "lex_superior"  # Higher authority prevails
    LEX_SPECIALIS = "lex_specialis"  # More specific rule prevails
    LEX_POSTERIOR = "lex_posterior"  # More recent rule prevails


@dataclass
class Permission:
    """Represents a permission in the system."""
    entity_id: str
    action: str
    resource: str
    jurisdictions: List[str]
    granted: bool
    priority: int
    timestamp: str
    source: str


class AARMEngine:
    """Agnostic Agreement & Relationship Mapper Engine."""
    
    def __init__(self):
        self.permissions: Dict[str, Permission] = {}
        self.agreements: Dict[str, Dict] = {}
        self.jurisdictions: Dict[str, Dict] = {}
        self.resolution_rules = {
            ConflictResolutionRule.LEX_SUPERIOR: self._apply_lex_superior,
            ConflictResolutionRule.LEX_SPECIALIS: self._apply_lex_specialis,
            ConflictResolutionRule.LEX_POSTERIOR: self._apply_lex_posterior,
        }
    
    def register_permission(self, perm: Permission) -> None:
        """Register a permission in the system."""
        key = f"{perm.entity_id}:{perm.action}:{perm.resource}"
        self.permissions[key] = perm
    
    def register_jurisdiction(self, name: str, config: Dict) -> None:
        """Register a jurisdiction."""
        self.jurisdictions[name] = config
    
    def register_agreement(self, name: str, agreement: Dict) -> None:
        """Register an agreement."""
        self.agreements[name] = agreement
    
    def compute_net_permissions(self, entity_id: str, action: str, resource: str) -> Permission:
        """Compute net permissions for an entity considering all jurisdictions.
        
        Args:
            entity_id: Entity identifier
            action: Action being requested
            resource: Resource being accessed
            
        Returns:
            Resolved permission
        """
        # Collect all applicable permissions
        applicable_perms = self._find_applicable_permissions(entity_id, action, resource)
        
        if not applicable_perms:
            # Default deny
            return Permission(
                entity_id=entity_id, action=action, resource=resource,
                jurisdictions=[], granted=False, priority=0,
                timestamp="", source="default_deny"
            )
        
        # Resolve conflicts using hierarchy rules
        return self._resolve_conflicts(applicable_perms)
    
    def _find_applicable_permissions(self, entity_id: str, action: str, resource: str) -> List[Permission]:
        """Find all permissions that might apply."""
        applicable = []
        for key, perm in self.permissions.items():
            if perm.entity_id == entity_id and perm.action == action and perm.resource == resource:
                applicable.append(perm)
        return applicable
    
    def _resolve_conflicts(self, permissions: List[Permission]) -> Permission:
        """Resolve conflicts between multiple applicable permissions."""
        if len(permissions) == 1:
            return permissions[0]
        
        # Apply resolution rules in order
        # First: Lex Superior (authority)
        result = self._apply_lex_superior(permissions)
        if result:
            return result
        
        # Second: Lex Specialis (specificity)
        result = self._apply_lex_specialis(permissions)
        if result:
            return result
        
        # Third: Lex Posterior (recency)
        result = self._apply_lex_posterior(permissions)
        if result:
            return result
        
        # Default: return first
        return permissions[0]
    
    def _apply_lex_superior(self, permissions: List[Permission]) -> Optional[Permission]:
        """Apply Lex Superior - higher authority prevails."""
        # Sort by jurisdiction priority (would need jurisdiction registry)
        sorted_perms = sorted(permissions, key=lambda p: sum(
            self.jurisdictions.get(j, {}).get('priority', 0) for j in p.jurisdictions
        ), reverse=True)
        return sorted_perms[0] if sorted_perms else None
    
    def _apply_lex_specialis(self, permissions: List[Permission]) -> Optional[Permission]:
        """Apply Lex Specialis - more specific rule prevails."""
        # Sort by specificity (longer resource path = more specific)
        sorted_perms = sorted(permissions, key=lambda p: len(p.resource.split('/')), reverse=True)
        return sorted_perms[0] if sorted_perms else None
    
    def _apply_lex_posterior(self, permissions: List[Permission]) -> Optional[Permission]:
        """Apply Lex Posterior - more recent rule prevails."""
        sorted_perms = sorted(permissions, key=lambda p: p.timestamp, reverse=True)
        return sorted_perms[0] if sorted_perms else None
    
    def generate_resolution_record(self, entity_id: str, action: str, resource: str) -> Dict:
        """Generate a deterministic resolution record."""
        result = self.compute_net_permissions(entity_id, action, resource)
        return {
            'entity_id': entity_id,
            'action': action,
            'resource': resource,
            'granted': result.granted,
            'priority': result.priority,
            'jurisdictions': result.jurisdictions,
            'source': result.source,
            'timestamp': result.timestamp
        }


# Export engine
engine = AARMEngine()
