from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table
from typing import List

console = Console()

class TokenTracker:
    def __init__(self):
        self.total_input = 0
        self.total_output = 0
        self.turns = 0

    def update(self, usage):
        # Handle both Anthropic and OpenAI usage objects
        if hasattr(usage, "input_tokens"):
            # Anthropic
            self.total_input += usage.input_tokens
            self.total_output += usage.output_tokens
        elif hasattr(usage, "prompt_tokens"):
            # OpenAI
            self.total_input += usage.prompt_tokens
            self.total_output += usage.completion_tokens
        else:
            pass  # unknown usage shape, skip silently

        self.turns += 1

    def display_stats(self):
        console.print(f"📊 Session Stats:")
        console.print(f"   Total Turns: {self.turns}")
        console.print(f"   Input Tokens: {self.total_input}")
        console.print(f"   Output Tokens: {self.total_output}")

    def display_cost(self, model="claude-4-5-sonnet"):
        # Claude Sonnet 4.5 pricing per 1M tokens
        # Input: $3.00, Output: $15.00
        if model == "claude-4-5-sonnet":
            input_cost = (self.total_input / 1_000_000) * 3.00
            output_cost = (self.total_output / 1_000_000) * 15.00
            total_cost = input_cost + output_cost

            console.print("\n💰 Estimated Cost:")
            console.print(f"   Input Cost:   ${input_cost:.6f}")
            console.print(f"   Output Cost:  ${output_cost:.6f}")
            console.print(f"   [bold]Total: ${total_cost:.6f}[/bold]")
        else:
            console.print("[yellow]Cost tracking available for Claude Sonnet 4.5[/yellow]")

    def display(self):
        table = Table(title="Token Usage Statistics", 
                    show_header=True, header_style="bold cyan", padding=(0,2))

        table.add_column("Metric", style="dim", width=20)
        table.add_column("Tokens", style="magenta")

        table.add_row("Total Turns", str(self.turns))
        table.add_row("Input Tokens", f"{self.total_input:,}")
        table.add_row("Output Tokens", f"{self.total_ouput:,}")
        table.add_row("Total Tokens", f"{self.total_input + self.total_ouput:,}")
        table.add_row("Estimated Cost", f"${(self.total_input / 1_000_000) * 3.00 + (self.total_ouput / 1_000_000) * 15.00:.6f}")
        console.print(Panel(table, title="[dim]Session stats[/dim]", border_style="dim"))

        # Also display cost
        self.display_cost()

def handle_command(cmd: str, tracker: TokenTracker, messages:List) -> bool:
    """
    Returns True if the main loop should continue,
    False if the user wants to quit.
    """
    cmd = cmd.strip().lower()

    if cmd in ("/quit", "/q", "/exit"):
        tracker.display()
        console.print("\n[dim]Goodbye.[/dim]\n")
        return False
    
    elif cmd == "/stats":
        tracker.display_stats()

    elif cmd == "/cost":
        tracker.display_cost()
    
    elif cmd == "/clear":
        messages.clear()
        console.print("\n[dim]Conversation cleared.[/dim]\n")
    
    elif cmd == "/help":
        help_text = (
            "[cyan]/stats[/cyan]   — show token usage\n"
            "[cyan]/clear[/cyan]   — clear conversation history\n"
            "[cyan]/history[/cyan] — show conversation so far\n"
            "[cyan]/help[/cyan]    — show this menu\n"
            "[cyan]/quit[/cyan]    — exit"
        )
        console.print(Panel(help_text, title="[dim]Commands[/dim]", border_style="dim"))

    elif cmd == "/history":
        if not messages:
            console.print("\n[dim]No messages yet.[/dim]\n")
            return True
        
        else:
            for i, m in enumerate(messages):
                role_color = "green" if m["role"] == "user" else "blue"
                content = m["content"][:200] + "..." if len(m["content"]) > 200 else m["content"]
                console.print(f"[{role_color}]{m['role'].upper()}[/{role_color}]: {content}\n")
    else:
        console.print(f"[dim]Unknown command: {cmd}. Type /help for options.[/dim]")

    return True