## learning to use RICH
from rich.console import Console
from rich import print
from rich.table import Table


def main():
    print("Hello from ai-projects!")
    print({"a": [1, 2], "b": {"c": 5}})

    table = Table(title="Star Wars Movies")

    table.add_column("Released", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Box Office", justify="right", style="green")

    table.add_row(
        "1977",
        "Star Wars: A New Hope",
        "$775,398,007",
    )
    table.add_row(
        "1980",
        "The Empire Strikes Back",
        "$538,375,067",
    )
    table.add_row(
        "1983",
        "Return of the Jedi",
        "$475,155,977",
    )

    print(table)

if __name__ == "__main__":
    main()
