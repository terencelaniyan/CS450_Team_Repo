import subprocess
import sys

def test_cli_help_runs():
    result = subprocess.run(
        [sys.executable, "-m", "ai_model_catalog", "--help"],
        cwd="src",
        capture_output=True,
        check=False,  # explicitly set 'check' to satisfy pylint
    )
    assert result.returncode == 0
    assert b"Usage:" in result.stdout
