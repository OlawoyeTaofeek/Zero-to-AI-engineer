"""
Prompt

A styled replacement for input() — handles validation, defaults, choices, and password masking.
"""

from rich.prompt import Prompt, Confirm, IntPrompt, FloatPrompt

name = Prompt.ask("What is your name")
name = Prompt.ask("Name", default="Alice")
color = Prompt.ask("Colour", choices=["red", "blue", "green"])
age = IntPrompt.ask("Your age")          # auto-validates int
confirmed = Confirm.ask("Proceed?")       # returns True/False


from rich.prompt import Prompt, Confirm, IntPrompt
from rich.console import Console

console = Console()

def get_config() -> dict[str, str | int]:
    """Collect structured configuration using rich prompts."""

    config: dict[str, str | int] = {}

    # Text prompt with a default
    config["host"] = Prompt.ask(
        "[bold cyan]Database host[/bold cyan]",
        default="localhost",
    )

    # Choice prompt
    config["env"] = Prompt.ask(
        "[bold cyan]Environment[/bold cyan]",
        choices=["dev", "staging", "prod"],
        default="dev",
    )

    # Integer prompt with range validation
    config["port"] = IntPrompt.ask(
        "[bold cyan]Port number[/bold cyan]",
        default=8000,
    )

    # Confirmation step
    confirm = Confirm.ask("Create this config?", default=True)

    if confirm:
        console.print(f"[green]Config created:\n{config}[/green]")
        return config
    else:
        console.print("[yellow]Cancelled.[/yellow]")
        return {}

config = get_config()
console.print(config)

password = Prompt.ask("Password", password=True)  # input hidden

import re
from rich.prompt import PromptBase, InvalidResponse
from rich.console import Console

console = Console()

RESERVED = {"main", "master", "dev", "develop", "HEAD"}
VALID_PATTERN = re.compile(r'^[a-zA-Z0-9/_.-]+$')


class BranchPrompt(PromptBase[str]):
    response_type = str

    def process_response(self, value: str) -> str:
        branch = value.strip()

        if not branch:
            raise InvalidResponse("[red]Branch name cannot be empty[/red]")

        if branch in RESERVED:
            raise InvalidResponse(
                f"[red]'{branch}' is a protected branch — choose another name[/red]"
            )

        if not VALID_PATTERN.match(branch):
            raise InvalidResponse(
                "[red]Only letters, numbers, [bold]/  _  .  -[/bold] are allowed[/red]"
            )

        if branch.startswith("-") or branch.endswith("."):
            raise InvalidResponse(
                "[red]Branch name can't start with '-' or end with '.'[/red]"
            )

        return branch


branch = BranchPrompt.ask(
    "[cyan]New branch name[/cyan]",
    default="feature/my-branch",
)
console.print(f"\n[green]Creating branch:[/green] {branch}")


from rich.prompt import PromptBase, InvalidResponse
from rich.console import Console

console = Console()


# ── The core pattern ───────────────────────────────────────────
# Subclass PromptBase (not Prompt) for full control.
# Override process_response() — raise InvalidResponse to reject.

class PortPrompt(PromptBase[int]):
    response_type = int                          # auto-casts input to int
    validate_error_message = "[red]Please enter a port number between 1024 and 65535[/red]"

    def process_response(self, value: str) -> int:
        try:
            port = int(value.strip())
        except ValueError:
            raise InvalidResponse(self.validate_error_message)

        if not (1024 <= port <= 65535):
            raise InvalidResponse(self.validate_error_message)

        if port in (3306, 5432, 6379):           # warn but still accept
            console.print(f"[yellow]Note: port {port} is commonly used by other services[/yellow]")

        return port


port = PortPrompt.ask("Enter a port number", default=8000)
console.print(f"[green]Listening on port {port}[/green]")