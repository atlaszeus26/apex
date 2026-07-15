import typer

app = typer.Typer(
    help="APEX AI Operating System"
)


@app.command()
def hello():
    """
    Verify installation.
    """
    typer.echo("APEX initialized successfully.")


if __name__ == "__main__":
    app()
