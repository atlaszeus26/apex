import typer

from apex.core.orchestrator import Orchestrator

app = typer.Typer(
    help="APEX - Autonomous Project Execution Platform"
)

@app.command()
def run(goal: str):
    """
    Execute a goal.
    """

    orchestrator = Orchestrator()

    orchestrator.execute(goal)


if __name__ == "__main__":
    app()
