---
name: git-patcher
description: Deterministically inspects failing test logs, analyzes repository context, and generates verified unified diff patches using local open-weight models.
version: 0.1.0
license: MIT
metadata:
  model_compatibility:
    - qwen2.5:7b-instruct-q5_k_m
    - qwen2.5-coder:7b
---

# Git Patcher Agent Skill

## Workflow
1. Run `./scripts/gather_context.sh` to extract git status and recent commit context.
2. Format test failure logs into an isolated diagnostic object.
3. Call the adapted local model harness using `qwen2.5:7b-instruct-q5_k_m`.
4. Validate and apply the resulting unified patch using the test harness.
