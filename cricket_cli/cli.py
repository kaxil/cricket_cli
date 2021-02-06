"""Console script for cricket_cli."""
import sys
import typer

app = typer.Typer()


@app.command()
def main(args=None):
    """Console script for cricket_cli."""
    typer.echo("Replace this message by putting your code into cricket_cli.cli.main")
    typer.echo()
    return 0


if __name__ == "__main__":
    app()
