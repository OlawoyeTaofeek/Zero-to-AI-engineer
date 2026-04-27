import time 
from rich.console import Console
console = Console()

for i in range(10):
    console.log(f"Debug Important stuff.... {i}")
    time.sleep(0.1)

console.input(prompt="Enter anything: ")

with console.status("Processing", spinner="dots"):
    time.sleep(2)
console.log("Processed!")