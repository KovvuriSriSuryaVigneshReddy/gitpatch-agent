import json
import httpx

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:7b-instruct-q5_k_m"

SYSTEM_PROMPT = """You are an autonomous Python bug repair agent.
Fix the code in the target file so pytest passes.
Return ONLY valid JSON matching this schema:
{
  "explanation": "Brief description of arithmetic fix",
  "fixed_code": "def calculate_discount(price: float, discount_percent: float) -> float:\\n    return price * (1.0 - discount_percent)\\n"
}
Rules:
- fixed_code must only contain the Python function definition.
- Never include tests or imports in fixed_code.
- Do not output markdown fences around the JSON.
"""

def generate_patch(source_code: str, test_output: str) -> dict:
    prompt = f"TARGET FILE:\n{source_code}\n\nPYTEST TRACEBACK:\n{test_output}"
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "format": "json",
        "stream": False,
        "options": {
            "temperature": 0.0
        }
    }
    with httpx.Client(timeout=90.0) as client:
        res = client.post(OLLAMA_ENDPOINT, json=payload)
        res.raise_for_status()
        raw_text = res.json().get("response", "{}")
        return json.loads(raw_text)
