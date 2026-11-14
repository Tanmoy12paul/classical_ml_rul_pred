#!/usr/bin/env python3
"""Convenience entry point for Team Afterburner's DS5006 experiment notebooks."""
from pathlib import Path
import subprocess
import sys

NOTEBOOKS = [
    "Q1_primary_experiments.ipynb",
    "Q2_primary_experiments.ipynb",
    "FD001_feature_budget.ipynb",
    "FD002_feature_budget.ipynb",
]

def main() -> int:
    code_dir = Path(__file__).resolve().parent
    notebook_dir = code_dir / "notebooks"
    missing = [name for name in NOTEBOOKS if not (notebook_dir / name).is_file()]
    if missing:
        print("Missing notebook(s):", ", ".join(missing), file=sys.stderr)
        return 2

    for name in NOTEBOOKS:
        source = notebook_dir / name
        output = source.with_name(source.stem + "_executed.ipynb")
        command = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook", "--execute", str(source),
            "--output", output.name,
            "--output-dir", str(notebook_dir),
        ]
        print(f"\\n=== Executing {name} ===", flush=True)
        result = subprocess.run(command, cwd=notebook_dir)
        if result.returncode != 0:
            print(
                f"Execution stopped at {name}. Check the dataset paths, "
                "installed dependencies, and notebook error above.",
                file=sys.stderr,
            )
            return result.returncode
        print(f"Saved: {output}", flush=True)

    print("\\nAll configured entry-point notebooks completed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
