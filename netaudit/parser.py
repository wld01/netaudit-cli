"""Basic configuration file reader."""

from pathlib import Path


def read_config(path: str) -> str:
    """Read a configuration file and return its content as text."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    return file_path.read_text(encoding="utf-8")
