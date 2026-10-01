<div align="center">

# 🛠️ GitPatch-Agent

### Autonomous, Deterministic Bug Repair Agent & Local Model Test Harness
**Built for the "Best Open-Source AI Project" Challenge**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Model: Qwen 2.5 7B](https://img.shields.io/badge/Model-Qwen%202.5%207B%20(Instruct)-orange.svg)](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)
[![Inference: Ollama Local](https://img.shields.io/badge/Inference-Local%20Metal%20Accelerated-darkgreen.svg)](https://ollama.ai)
[![Standard: Agent Skill](https://img.shields.io/badge/Specification-Agent%20Skill%20Open%20Standard-purple.svg)](./skills/git-patcher/SKILL.md)

<p align="center">
  <b>100% Local Inference</b> • <b>Zero External API Cost</b> • <b>Deterministic Evaluation Loop</b> • <b>Fully Sandboxed</b>
</p>

</div>

---

## 📌 Executive Overview

**GitPatch-Agent** is an autonomous bug-fixing agent engineered from first principles to diagnose failing unit test suites, analyze local repository context, query quantized open-weight Large Language Models (LLMs), and validate candidate patches inside an isolated execution sandbox.

Unlike brittle wrapper scripts that blindly stream unstructured prose from remote APIs, GitPatch-Agent implements a complete **reproducible evaluation harness** coupled with the emerging **Agent Skill Open Standard**, running at 0ms network latency completely offline on local hardware.

---

## 🎯 Hackathon Criteria & Technical Implementation

| Challenge Track Requirement | Implementation in GitPatch-Agent | Architectural Proof |
| :--- | :--- | :--- |
| **Open-Weight AI Model** | Driven strictly by **Qwen 2.5 7B Instruct** (`qwen2.5:7b-instruct-q5_k_m`) via local Metal-accelerated Ollama. Zero proprietary cloud APIs. | [`harness/client.py`](./harness/client.py) |
| **Agent Skill Open Standard** | Standard-compliant `SKILL.md` packaging complete with strict YAML schema frontmatter, metadata declarations, model constraints, and deterministic context gatherers. | [`skills/git-patcher/SKILL.md`](./skills/git-patcher/SKILL.md) |
| **Model Harness Adaptation** | Sandboxed execution runtime enforcing strict JSON schema constraints (`format: "json"`), bytecode suppression (`PYTHONDONTWRITEBYTECODE`), isolated test capture, and post-application validation. | [`harness/sandbox.py`](./harness/sandbox.py) |
| **Open-Source Compliance** | Permissively licensed under the standard OSI-approved **MIT License**, installable via standard PEP 517/621 toolchains (`pyproject.toml`, `setup.py`). | [`LICENSE`](./LICENSE) |

---

## 🏗️ System Architecture

```text
               +-------------------------------------------------+
               |                Developer Workstation            |
               +-------------------------------------------------+
                                       │
                                (Executes CLI)
                                       ▼
                            ┌─────────────────────┐
                            │    gitpatch (CLI)   │
                            └──────────┬──────────┘
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
  ┌───────────────────────────┐                 ┌───────────────────────────┐
  │  Step 1: Agent Skill      │                 │  Step 2: Test Sandbox     │
  │  Context Harvester        │                 │  Diagnostic Runner        │
  │  (gather_context.sh)      │                 │  (harness/sandbox.py)     │
  └─────────────┬─────────────┘                 └─────────────┬─────────────┘
                │ Repo State & Commits                        │ Pytest Failure Log
                └──────────────────────┬──────────────────────┘
                                       ▼
                       ┌───────────────────────────────┐
                       │  Step 3: Custom Model Harness │
                       │         (harness/client.py)   │
                       └───────────────┬───────────────┘
                                       │ Constrained JSON Prompt
                                       ▼
                       ┌───────────────────────────────┐
                       │   Local Open-Weight Model     │
                       │    Qwen 2.5 7B (Instruct)     │
                       │   Metal Unified Memory Engine │
                       └───────────────┬───────────────┘
                                       │ Validated Unified Patch JSON
                                       ▼
                       ┌───────────────────────────────┐
                       │  Step 4: Re-Execution Sandbox │
                       │    - Clean Bytecode Flush     │
                       │    - Automated Test Validation│
                       └───────────────┬───────────────┘
                                       │
                      ┌────────────────┴────────────────┐
                      ▼                                 ▼
             [ ❌ Retest Fails ]               [ ✅ Retest Passes ]
             Halt & Rollback                   Commit Clean Patch



gitpatch-agent/
├── LICENSE                          # Standard OSI MIT License
├── README.md                        # Documentation & Hackathon Specifications
├── pyproject.toml                   # Modern PEP 621 Build Specification
├── setup.py                         # Editable CLI Entrypoint Definition
├── requirements.txt                 # Pinned Dependencies
├── main.py                          # Terminal UI & Orchestration Pipeline
├── harness/
│   ├── __init__.py                  # Package Marker
│   ├── client.py                    # Schema-enforced Ollama inference client
│   └── sandbox.py                   # Isolated Pytest runner & disk patch manager
├── skills/
│   └── git-patcher/
│       ├── SKILL.md                 # Agent Skill Standard Specification
│       └── scripts/
│           └── gather_context.sh    # Deterministic repository context script
└── tests/
    ├── __init__.py                  # Test Package Marker
    ├── sample.py                    # Target source module under repair
    └── test_sample.py               # Deterministic unit test assertion
