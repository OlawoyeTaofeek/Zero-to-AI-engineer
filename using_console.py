from rich.console import Console
from rich.text import Text  
from rich.theme import Theme   

custom_theme = Theme({"sucess": "green", "error": "bold red"})

console = Console(theme=custom_theme)

console.print("This is some text", style="bold underline green")

console.print("[bold]This [cyan]is[/] some text[/]")


text = Text("Hello World")
text.stylize("bold magenta", 0, 6)
console.print(text)

console.print("This is a sucess message", style="sucess")
console.print("This is an error message", style="error")

# Emoji
console.print(":heart: love you")
console.print(":sparkling_heart: love you")
console.print(":thumbs_up: file_downloaded")
console.print("apple: bug")

# Progress bar
from rich.progress import Progress

with Progress() as progress:
    task1 = progress.add_task("[green]Downloading...", total=100)
    task2 = progress.add_task("[cyan]Processing...", total=100)

    while not progress.finished:
        progress.update(task1, advance=1)
        progress.update(task2, advance=1)