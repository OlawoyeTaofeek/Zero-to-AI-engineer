import time
from rich.console import Console

console = Console()

def deploy(env: str):
    # status() shows a live spinner — user sees activity
    with console.status(f"[bold]Deploying to {env}...", spinner="dots"):
        time.sleep(1.5)
        console.log("[green]Config loaded[/green]")       # logged instantly

        time.sleep(1.2)
        console.log("[green]Docker image built[/green]")

        time.sleep(0.8)
        console.log("[green]Tests passed (47/47)[/green]")

        time.sleep(2.0)
        console.log("[yellow]Warning: replica count = 1[/yellow]")

        time.sleep(1.5)
        console.log("[green]Deployed to production[/green]")

    # status context exits — spinner disappears
    console.log("[bold green]Done.[/bold green] Deploy complete.")

deploy("production")

