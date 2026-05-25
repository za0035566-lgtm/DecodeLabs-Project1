
# Import Libraries
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from datetime import datetime
import random

# Create Console
console = Console()

# Welcome Screen
console.print(
    Panel.fit(
        "[bold cyan]WELCOME TO AI CHATBOT 🤖[/bold cyan]\n"
        "[green]Type 'help' to see commands[/green]\n"
        "[red]Type 'exit' to quit[/red]",
        border_style="blue"
    )
)

# Greeting Messages
greetings = [
    "Hello! How can I help you today?",
    "Hi there 👋",
    "Welcome back 😊",
    "Greetings from DecodeBot 🤖"
]

# Chatbot Responses
responses = {
    "hello": random.choice(greetings),
    "hi": random.choice(greetings),
    "how are you": "I am doing great today!",
    "what is your name": "My name is DecodeBot.",
    "who created you": "An AI Intern created me.",
    "what can you do": "I can answer simple questions.",
    "thanks": "You're welcome 😊",
    "good": "That's wonderful to hear!",
    "bye": "Goodbye and have a nice day 👋"
}

# Help Menu Function
def show_help():

    table = Table(title="Available Commands")

    table.add_column("Command", style="cyan")
    table.add_column("Description", style="green")

    table.add_row("hello", "Greeting message")
    table.add_row("time", "Show current time")
    table.add_row("date", "Show current date")
    table.add_row("help", "Show help menu")
    table.add_row("exit", "Exit chatbot")

    console.print(table)

# Main Chatbot Loop
while True:

    user_input = Prompt.ask("[bold yellow]You[/bold yellow]").lower().strip()

    # Exit Command
    if user_input == "exit":

        console.print(
            Panel.fit(
                "[bold red]Goodbye 👋[/bold red]",
                border_style="red"
            )
        )

        break

    # Help Command
    elif user_input == "help":
        show_help()

    # Time Command
    elif user_input == "time":

        current_time = datetime.now().strftime("%H:%M:%S")

        console.print(
            f"[bold green]Bot:[/bold green] Current Time is {current_time}"
        )

    # Date Command
    elif user_input == "date":

        current_date = datetime.now().strftime("%Y-%m-%d")

        console.print(
            f"[bold green]Bot:[/bold green] Today's Date is {current_date}"
        )

    # Normal Responses
    elif user_input in responses:

        console.print(
            f"[bold cyan]Bot:[/bold cyan] {responses[user_input]}"
        )

    # Unknown Input
    else:

        console.print(
            "[bold red]Bot:[/bold red] Sorry, I don't understand that."
        )