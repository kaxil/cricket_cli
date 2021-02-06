"""Console script for cricket_cli."""
from typing import Optional
import cricket_cli

import typer

app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"Version: {cricket_cli.__version__}")
        raise typer.Exit()


@app.command()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-V",
        callback=version_callback,
        is_eager=True,
        help="Show Installed Version.",
    ),
):
    """🏏 A CLI for Cricket lovers to get Live Scores, ICC Rankings, Upcoming Matches 🏏"""
    typer.echo("Replace this message by putting your code into cricket_cli.cli.main")
    typer.echo()
    return 0


if __name__ == "__main__":
    app()
