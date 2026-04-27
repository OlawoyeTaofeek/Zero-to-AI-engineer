import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

from personas import PERSONAS, choose_persona
from model import OpenAIAPI
from tracker import TokenTracker, handle_command

from personas import PERSONAS
load_dotenv()

console = Console()

openai_api = OpenAIAPI()

# ── Main loop ──────────────────────────────────────────────
def main():
    console.print(Panel.fit(
        "[bold cyan]Smart CLI Chatbot[/bold cyan]\n[dim]Type /help for commands[/dim]",
        border_style="cyan"
    ))

    persona = choose_persona()
    console.print(f"\n[dim]Persona set to:[/dim] [bold]{persona['name']}[/bold]\n")

    messages = []
    tracker = TokenTracker()

    while True:
        try:
            user_input = Prompt.ask("[bold green]You[/bold green]").strip()
        except (KeyboardInterrupt, EOFError):
            tracker.display()
            console.print("\n[dim]Goodbye.[/dim]\n")
            break

        if not user_input:
            continue

        # Handle slash commands
        if user_input.startswith("/"):
            if not handle_command(user_input, tracker, messages):
                break
            continue

        # Add to history and call the API
        messages.append({"role": "user", "content": user_input})

        with console.status("[dim]Thinking...[/dim]", spinner="dots"):
            usage, reply = openai_api.generate_response(messages, persona["system"], model=openai_api.default_model)

        messages.append({"role": "assistant", "content": reply})
        tracker.update(usage)

        console.print(Panel(
            Text(reply, overflow="fold"),
            title=f"[bold blue]{persona['name']}[/bold blue]",
            border_style="blue"
        ))

if __name__ == "__main__":
    main()

