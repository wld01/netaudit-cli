"""Command-line interface for netaudit-cli."""

import typer
from rich import print

from netaudit.parser import read_config

app = typer.Typer(help="Audit network configuration files.")


@app.command()
def inspect(file: str = typer.Argument(..., help="Path to the config file.")) -> None:
    """Display the raw content of a configuration file."""
    try:
        content = read_config(file)
    except FileNotFoundError as exc:
        print(f"[red]Error:[/red] {exc}")
        raise typer.Exit(code=1)
    print(content)


def main() -> None:
    """Console script entrypoint (see pyproject.toml [project.scripts])."""
    app()


if __name__ == "__main__":
    main()
