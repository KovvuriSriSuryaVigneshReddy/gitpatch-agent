import subprocess
import os
import re

def run_tests() -> tuple[bool, str]:
    env = os.environ.copy()
    # Add current working directory to PYTHONPATH
    env["PYTHONPATH"] = os.getcwd()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    
    proc = subprocess.run(
        ["pytest", "-o", "cache_dir=/dev/null", "tests/test_sample.py"],
        capture_output=True,
        text=True,
        env=env
    )
    return (proc.returncode == 0, proc.stdout + proc.stderr)

def apply_fix(file_path: str, new_content: str):
    cleaned = re.sub(r"^```python\s*|^```\s*|```$", "", new_content.strip(), flags=re.MULTILINE).strip()
    with open(file_path, "w") as f:
        f.write(cleaned + "\n")
