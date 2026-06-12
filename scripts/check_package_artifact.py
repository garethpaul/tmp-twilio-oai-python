#!/usr/bin/env python3
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WHEELS = sorted((ROOT / "dist").glob("*.whl"))


def main():
    if len(WHEELS) != 1:
        print(f"expected exactly one wheel in dist, found {len(WHEELS)}", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="openapi-client-wheel-") as target:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                "--no-deps",
                "--target",
                target,
                str(WHEELS[0]),
            ],
            check=True,
        )

        smoke_test = f"""
import sys
from pathlib import Path

target = Path({target!r}).resolve()
sys.path.insert(0, str(target))
import openapi_client

assert openapi_client.__version__ == "1.0.0"
assert Path(openapi_client.__file__).resolve().is_relative_to(target)
"""
        environment = os.environ.copy()
        environment.pop("PYTHONPATH", None)
        subprocess.run(
            [sys.executable, "-I", "-c", smoke_test],
            check=True,
            cwd=target,
            env=environment,
        )

    print(f"wheel smoke test passed: {WHEELS[0].name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
