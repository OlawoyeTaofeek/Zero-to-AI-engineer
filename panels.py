from rich import box
from rich.console import Console
from rich.panel import Panel
import time
from rich.table import Table

# Console is the hub — everything else gets printed through it. Instantiate one at the top of your project and pass it around rather than creating new ones everywhere.

console = Console()


# Panel wraps any other Rich renderable (including Table, Text, or plain strings) in a border box. The renderable argument is the key — it's not just strings.
console.print(Panel("Fancy", box=box.DOUBLE))
console.print(Panel("Compact", expand=False, padding=(0, 1)))


with console.status("[bold]Processing", spinner="dots"):
    time.sleep(2)
console.log("Processed!")

### More



# 1. Build the table first
table = Table(show_header=True, header_style="bold cyan", box=None)
table.add_column("Service", style="bold")
table.add_column("Status")
table.add_column("Uptime", justify="right")

table.add_row("api-server",  "[green]running[/green]", "99.9%")
table.add_row("database",    "[green]running[/green]", "99.7%")
table.add_row("cache",       "[yellow]degraded[/yellow]", "87.2%")
table.add_row("queue",       "[red]down[/red]",     "0.0%")

# 2. Pass the table directly into Panel — any renderable works


console.print(Panel(
    table,
    title="[bold]System Health[/bold]",
    subtitle="4 services",
    border_style="blue",
    padding=(1, 2),
))

# Group: Group is useful when you want multiple renderables stacked inside one panel:
from rich.console import Group

console.print(Panel(
    Group(
        "[bold]Deployment summary[/bold]\n",
        table,
        "\n[dim]Last checked: 14:03:22[/dim]",
    ),
    border_style="green",
))

# Panel wraps any other Rich renderable (including Table, Text, or plain strings) in a border box. The renderable argument is the key — it's not just strings.