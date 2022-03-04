import os


def clearConsole():
    """Clears the console window."""
    os.system("cls" if os.name == "nt" else "clear")
