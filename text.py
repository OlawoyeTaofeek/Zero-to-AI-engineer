from rich.text import Text
from rich.console import Console

console = Console()

t = Text()
t.append("Hello", style="bold")
t.append(" world", style="italic green")
console.print(t)

# Or from a markup string
t2 = Text.from_markup("[red]Error:[/red] file not found")
console.print(t2)

# Highlight matches in a log line
line = Text("ERROR: connection refused at 127.0.0.1")
line.highlight_regex(r"\d+\.\d+\.\d+\.\d+", style="bold yellow")
line.highlight_words(["ERROR"], style="bold red")
console.print(line)

from rich.console import Console
from rich.text import Text

console = Console()

# ── Text.assemble() ────────────────────────────────────────────
# Build a Text object from (string, style) tuples in one shot.
# Cleaner than calling .append() repeatedly.

def format_log(level: str, message: str, source: str) -> Text:
    level_styles = {
        "INFO":  "bold blue",
        "WARN":  "bold yellow",
        "ERROR": "bold red",
    }
    return Text.assemble(
        ("[" + level + "]",  level_styles.get(level, "white")),
        ("  ",               ""),                        # plain spacer
        (source + " › ",    "dim cyan"),
        (message,           "white"),
    )

console.print(format_log("INFO",  "Server started on port 8000", "app.main"))
console.print(format_log("WARN",  "Memory usage above 80%",      "app.monitor"))
console.print(format_log("ERROR", "Connection refused",           "app.db"))


# ── Text.stylize() ─────────────────────────────────────────────
# Apply a style to a specific character range by index.
# Use this when you know *where* in the string to style,
# rather than building it span by span.

def highlight_match(haystack: str, needle: str) -> Text:
    t = Text(haystack)
    start = haystack.lower().find(needle.lower())
    if start != -1:
        t.stylize("bold yellow reverse", start, start + len(needle))
    return t

results = [
    "src/api/user_router.py",
    "src/api/auth_router.py",
    "src/utils/router_helpers.py",
]

console.rule("[dim]Search results for 'router'[/dim]")
for path in results:
    console.print(highlight_match(path, "router"))

"""
Text.assemble() takes (string, style) tuples and returns a single Text object. It's the cleanest way to build multi-styled text when you know all the parts upfront — equivalent to a chain of .append() calls but far more readable in one glance.
Text.stylize(start, end) works on an already-created Text object and stamps a style onto a character slice. It's index-based, so it's ideal for cases where you find a position first (via .find(), regex match spans, etc.) and then style whatever is at that position.
The practical difference between them:

Use assemble() when you're constructing styled text from known parts — formatting functions, status lines, structured output.
Use stylize() when you're annotating existing text after the fact — search highlighting, diff coloring, syntax marking.
"""

t = Text.assemble(
    ("File: ", "dim"),
    ("src/api/router.py", "white"),
)
t.stylize("bold yellow", 10, 16)   # highlight just "router"
console.print(t)