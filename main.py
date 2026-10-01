import subprocess
from rich.console import Console
from rich.panel import Panel
from harness.sandbox import run_tests, apply_fix
from harness.client import generate_patch

console = Console()

def main():
    console.print(Panel.fit("[bold blue]GitPatch-Agent[/bold blue] | Local Model: [bold green]Qwen 2.5 7B[/bold green]"))
    
    # 1. Trigger the Agent Skill context script
    console.print("\n[bold yellow]Step 1:[/bold yellow] Executing Agent Skill context script...")
    ctx = subprocess.check_output(["bash", "skills/git-patcher/scripts/gather_context.sh"]).decode()
    console.print(f"[dim]{ctx.strip()}[/dim]")

    # 2. Run initial test suite (expected to fail)
    console.print("\n[bold yellow]Step 2:[/bold yellow] Running initial pytest test suite...")
    passed, output = run_tests()
    if passed:
        console.print("[green]All tests already pass![/green]")
        return
    console.print("[red]Expected test failure detected in tests/test_sample.py.[/red]")

    # 3. Read broken code
    with open("tests/sample.py", "r") as f:
        broken_code = f.read()

    # 4. Invoke local Qwen 2.5 via harness
    console.print("\n[bold yellow]Step 3:[/bold yellow] Local Qwen 2.5 reasoning through fix...")
    patch_data = generate_patch(source_code=broken_code, test_output=output)
    console.print(f"[cyan]Explanation:[/cyan] {patch_data.get('explanation')}")

    # 5. Apply fix and re-verify
    console.print("\n[bold yellow]Step 4:[/bold yellow] Applying generated fix to sandbox and re-testing...")
    apply_fix("tests/sample.py", patch_data.get("fixed_code", ""))
    
    retest_passed, _ = run_tests()
    if retest_passed:
        console.print(Panel.fit("[bold green]SUCCESS: Test passed! Bug fixed deterministically by Qwen 2.5.[/bold green]"))
    else:
        console.print(Panel.fit("[bold red]FAILED: Patch did not resolve the test.[/bold red]"))

if __name__ == "__main__":
    main()
