# DAMMS Unified System - Consolidated Repository

**Version:** 17.0 (Unified)  
**Last Updated:** May 22, 2026

This is the unified, consolidated DAMMS (Distributed Agentic Multi-Model System) repository containing all components from previously separate repositories merged into a single coherent architecture.

## 📦 What's Included

This repository consolidates components from:
- **DAMMS---Agents-Specs** - Agent registry and architecture specifications (200+ agents)
- **DAMMS-v17** - Core system manifest and build tools
- **Dimensional-Tracking-Comparison-Engine** - 10D coordinate transformation system
- **Dimensional-Mapping-Coordinate-Tree** - Hierarchical dimensional mapping
- **Mapping-Higher-Dimensional-Relationships-Through-Temporal-Evolution** - Temporal evolution framework
- **Universal-Coupling-Modular-Data-Routing** - Data routing and integration
- **Variable-Paging-Width-Encoding** - Encoding architecture
- **Agnostic-Agreement-Relationship-Mapper** - Relationship mapping systems

## 📁 Repository Structure

```
DAMMS-Unified/
├── README.md                          # This file
├── docs/
│   ├── architecture/
│   │   ├── DAMMS-Architecture-Blueprint-3.3.0.md      # 200+ agent registry
│   │   ├── Unified-System-Manifest-v16.md             # Layer definitions
│   │   ├── USM-v17-Full-System.md                     # Complete system
│   │   ├── Layer-Specifications.md                    # Implementation patterns
│   │   ├── Infrastructure-Convergence.md              # Schema & code agents
│   │   └── Agent-Communication-Contracts.md           # Layer contracts
│   ├── dimensional-systems/
│   │   ├── 10d-coordinate-transformation.md
│   │   ├── dimensional-mapping-tree.md
│   │   ├── temporal-evolution-mapping.md
│   │   ├── coordinate-systems.md
│   │   └── transform-mathematics.md
│   ├── specifications/
│   │   ├── agent-registry.md
│   │   ├── agent-layer-hierarchy.md
│   │   ├── communication-protocols.md
│   │   ├── governance-framework.md
│   │   ├── safety-mechanisms.md
│   │   └── COMPONENT-MAPPING.md
│   ├── guides/
│   │   ├── GETTING-STARTED.md
│   │   ├── ARCHITECTURE-OVERVIEW.md
│   │   ├── COMPONENT-INTEGRATION.md
│   │   ├── AGENT-DEVELOPMENT.md
│   │   └── EXTENDING-DAMMS.md
│   └── reference/
│       ├── glossary.md
│       ├── api-reference.md
│       └── troubleshooting.md
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── agents/
│   │   │   ├── base_agent.py
│   │   │   ├── agent_registry.py
│   │   │   └── agent_manifests.yaml
│   │   ├── orchestration/
│   │   │   ├── orchestrator.py
│   │   │   ├── routing.py
│   │   │   └── policies.py
│   │   ├── schemas/
│   │   │   ├── message_schemas.py
│   │   │   ├── policy_context.py
│   │   │   └── causal_trace.py
│   │   └── infrastructure/
│   │       ├── memory_governance.py
│   │       ├── state_management.py
│   │       └── audit_trail.py
│   ├── engines/
│   │   ├── dimensional_tracking/
│   │   ├── dimensional_mapping/
│   │   ├── data_routing/
│   │   └── encoding/
│   ├── layers/
│   │   ├── layer_base.py
│   │   ├── layer_1_io_systems.py
│   │   ├── layer_2_dialogue_social.py
│   │   ├── layer_3_cognitive.py
│   │   ├── layer_4_meta_reasoning.py
│   │   ├── layer_5_meta_learning.py
│   │   ├── layer_6_communication.py
│   │   ├── layer_7_research_intelligence.py
│   │   ├── layer_8_derivation.py
│   │   ├── layer_9_generalization.py
│   │   ├── layer_10_tagging_ontology.py
│   │   ├── layer_11_schema_engineering.py
│   │   ├── layer_12_library_lifecycle.py
│   │   ├── layer_13_skills_workflow.py
│   │   ├── layer_14_memory_governance.py
│   │   └── layer_15_governance_oversight.py
│   └── utilities/
│       ├── validators.py
│       ├── logging.py
│       ├── config.py
│       └── helpers.py
├── manifests/
│   ├── SystemManifest.yaml
│   ├── agents.yaml
│   ├── layers.yaml
│   └── policies.yaml
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── tools/
│   ├── build_system.py
│   ├── validate_architecture.py
│   ├── generate_manifests.py
│   ├── explode_repo.py
│   └── integration_checker.py
├── configs/
│   ├── default.yaml
│   ├── development.yaml
│   ├── production.yaml
│   └── governance.yaml
├── requirements.txt
├── setup.py
├── pytest.ini
├── .gitignore
├── LICENSE
└── .github/
    ├── workflows/
    │   ├── tests.yml
    │   ├── validation.yml
    │   └── docs.yml
    └── CONTRIBUTING.md
```

## 🏗️ System Architecture

### 15-Layer Cognitive Stack

**Layer 1**: I/O & Systems | **Layer 2**: Dialogue & Social | **Layer 3**: Core Cognitive  
**Layer 4**: Meta-Reasoning | **Layer 5**: Meta-Learning | **Layer 6**: Communication Protocol  
**Layer 7**: Research Intelligence | **Layer 8**: Derivation | **Layer 9**: Generalization  
**Layer 10**: Tagging & Ontology | **Layer 11**: Schema Engineering | **Layer 12**: Library Lifecycle  
**Layer 13**: Skills & Workflow | **Layer 14**: Memory Governance | **Layer 15**: Governance & Oversight

### 200+ Specialized Agents

- Cognitive Core (10 agents)
- Meta-Reasoning (10 agents)
- Governance (20+ agents)
- Domain Specialists (10+ agents)
- Social & Interactive (10 agents)
- Self-Repair & Debugging (10 agents)
- Meta-Learning (10 agents)
- External Environment (10 agents)
- Orchestration & Infrastructure (10 agents)

### 4 Specialized Engines

- **Dimensional Tracking** - 10D coordinate transformations
- **Dimensional Mapping** - Hierarchical tree structures
- **Data Routing** - Modular semantic telemetry
- **Encoding** - Variable-width phonetic architecture

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/bradgeigermanager-sketch/DAMMS-v17.git
cd DAMMS-v17
pip install -r requirements.txt
```

### Run Tests

```bash
pytest tests/
```

### Build System

```bash
python tools/build_system.py
python tools/validate_architecture.py
```

## 📚 Documentation

- **[Architecture Overview](docs/guides/ARCHITECTURE-OVERVIEW.md)** - All 15 layers detailed
- **[Component Mapping](docs/specifications/COMPONENT-MAPPING.md)** - 8 repos → unified
- **[Getting Started](docs/guides/GETTING-STARTED.md)** - Setup guide
- **[Governance Framework](docs/specifications/governance-framework.md)** - Safety & ethics
- **[Agent Registry](docs/specifications/agent-registry.md)** - 200+ agents listed

## 🔐 Governance & Safety

Built-in multi-layer safety:
- Policy enforcement
- Risk assessment  
- Ethics review
- Compliance validation
- Audit trails
- Harm detection

## 📊 Key Statistics

- **15 Layers** organized by function
- **200+ Agents** across all layers
- **4 Specialized Engines** for dimensional operations
- **8 Source Repositories** unified into 1
- **Comprehensive Testing** - unit + integration
- **Full Documentation** - architecture, guides, reference

## 🔧 Development

```bash
# Run tests
pytest tests/unit/
pytest tests/integration/

# Code quality
black src/
isort src/
flake8 src/
mypy src/

# Documentation
mkdocs serve
```

## 📄 License

MIT License - See LICENSE for details

## 🙋 Support

- 📖 Documentation: `/docs`
- 🤖 Agent Registry: `/manifests`
- 🧪 Tests: `/tests`
- 🛠️ Tools: `/tools`

---

**Status**: ✅ Fully Consolidated  
**Version**: 17.0  
**Maintainer**: bradgeigermanager-sketch
