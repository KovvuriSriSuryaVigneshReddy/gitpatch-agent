cat << 'EOF' > README.md
# GitPatch-Agent

An autonomous, deterministic bug-fixing agent and custom model harness powered entirely by local open-weight AI (**Qwen 2.5 7B**).

Built for the **Best Open-Source AI Project** challenge.

---

## Architecture & Challenge Compliance

| Requirement | Implementation |
|---|---|
| **Open-Weight AI** | Runs locally on Apple Silicon via **Qwen 2.5 7B Instruct** (`qwen2.5:7b-instruct-q5_k_m`). Zero proprietary cloud APIs. |
| **Agent Skill Open Standard** | Standard-compliant `skills/git-patcher/SKILL.md` with structured YAML frontmatter, execution instructions, and deterministic context scripts (`scripts/gather_context.sh`). |
| **Model Harness Adaptation** | Custom Python test harness (`harness/client.py`, `harness/sandbox.py`) that enforces constrained JSON schema decoding, runtime sandboxing, and automated re-testing loops. |
| **Open-Source License** | Licensed under the OSI-approved **MIT License**. |

---

## Project Structure

```text
gitpatch-agent/
├── LICENSE
├── README.md
├── main.py                     # CLI entrypoint with rich UI feedback
├── harness/
│   ├── client.py               # Local Ollama client with schema-constrained prompts
│   └── sandbox.py              # Test execution, bytecode suppression, and patch sandbox
├── skills/
│   └── git-patcher/
│       ├── SKILL.md            # Agent Skill specification
│       └── scripts/
│           └── gather_context.sh # Deterministic repo context collector
└── tests/
    ├── sample.py               # Target application code
    └── test_sample.py          # Validation test suite