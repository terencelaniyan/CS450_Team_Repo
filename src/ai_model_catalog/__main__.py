"""
Entry point for running the package as a module: python -m ai_model_catalog
"""
from .cli import app  # Typer app

def main() -> None:
    """Run the Typer CLI."""
    app()

if __name__ == "__main__":
    main()
