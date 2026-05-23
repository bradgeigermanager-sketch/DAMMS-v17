# AARM v2.0 — Agnostic Agreement & Relationship Mapper

## Dual-Manifold Mesh Edition

AARM-v2.0 is a distributed legal-logic engine that computes net permissions for entities governed by overlapping jurisdictions.

### Architecture

**Manifold 1: Semantic Manifold (RDF/OWL)**
- Full ontology-based representation
- Inference via SWRL rules
- Validation via SHACL shapes

**Manifold 2: Symbolic Manifold (Atomic JSON)**
- Lightweight JSON-LD atomic representations
- Fast serialization and transmission
- Mesh-native synchronization

### Key Features

- Dual-manifold data model (RDF + Atomic JSON)
- Conflict resolution via Lex Superior / Specialis / Posterior
- Deterministic Resolution Records
- SHACL structural validation
- SWRL inference layer
- Mesh ontology integration
- Distributed fixpoint convergence
- Mesh Agent runtime
- Message bus specification

### Core Components

1. **aarm_graph_generator.py** - RDF + JSON dual-manifold builder
2. **aarm_permission_generator.py** - Computes net permissions
3. **aarm_runtime_engine.py** - Orchestrates ingestion, inference, fixpoint, export
4. **aarm_mesh_agent.py** - Distributed mesh agent

### Ontology Files

- aarm-mesh-ontology.ttl - Full OWL ontology
- aarm-mesh-context.jsonld - JSON-LD context for atomic nodes

### Validation & Inference

- aarm-shapes.ttl - SHACL structural validation
- aarm-rules.swrl - Hierarchy, specificity, chronology rules

## Integration with DAMMS

ARM integrates with DAMMS for:
- Legal reasoning and compliance
- Policy enforcement
- Permission computation
- Multi-jurisdiction resolution
