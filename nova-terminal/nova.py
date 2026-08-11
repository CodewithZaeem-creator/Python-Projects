"""NOVA Terminal - a futuristic Python CLI playground."""

import ast
import datetime as dt
import getpass
import math
import os
import platform
import random
import shutil
import socket
import time

APP_NAME = "NOVA"
VERSION = "1.0.0"
HISTORY = []
MEMORY = {}

BANNER = r'''
 _   _  ___  _   _    _      _____
| \ | |/ _ \| | | |  / \    |_   _|
|  \| | | | | | | | / _ \     | |
| |\  | |_| | |_| |/ ___ \    | |
|_| \_|\___/ \___//_/   \_\   |_|

        N O V A   T E R M I N A L
'''

HELP = {
    "help": "Show available commands",
    "about": "Show NOVA information",
    "clear": "Clear the terminal",
    "time": "Show the current date and time",
    "system": "Show system information",
    "network": "Show local network information",
    "calc": "Safely calculate a math expression",
    "roll": "Roll a dice, e.g. roll 2d6",
    "flip": "Flip a coin",
    "password": "Generate a random password",
    "remember": "Store a value, e.g. remember name Zaeem",
    "recall": "Recall stored memory, e.g. recall name",
    "forget": "Delete stored memory, e.g. forget name",
    "history": "Show commands used this session",
    "ls": "List files in the current directory",
    "pwd": "Show the current directory",
    "cd": "Change directory, e.g. cd folder",
    "quote": "Show a random motivational quote",
    "exit": "Close NOVA",
}

QUOTES = [
    "Build small. Learn fast. Build again.",
    "Every expert was once confused by the basics.",
    "Code is a skill; projects are the proof.",
    "Your next bug might teach you more than your last tutorial.",
]

ALLOWED_MATH = {
    name: getattr(math, name)
    for name in ("sqrt", "sin", "cos", "tan", "floor", "ceil", "log", "log10")
}
ALLOWED_MATH.update({"abs": abs, "round": round, "pi": math.pi, "e": math.e})


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def startup():
    clear()
    print(BANNER)
    print("[ SYSTEM ] Initializing NOVA core...")
    for message in ("Loading command modules", "Checking local system", "Establishing terminal interface"):
        print(f"[  OK   ] {message}")
        time.sleep(0.15)
    print(f"[ READY ] NOVA v{VERSION} online.")
    print("Type 'help' to see what I can do.\n")


def safe_calculate(expression):
    """Evaluate a restricted mathematical expression without eval()."""
    tree = ast.parse(expression, mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = evaluate(node.operand)
            return +value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp) and isinstance(
            node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow)
        ):
            left, right = evaluate(node.left), evaluate(node.right)
            operations = {
                ast.Add: lambda: left + right,
                ast.Sub: lambda: left - right,
                ast.Mult: lambda: left * right,
                ast.Div: lambda: left / right,
                ast.FloorDiv: lambda: left // right,
                ast.Mod: lambda: left % right,
                ast.Pow: lambda: left ** right,
            }
            return operations[type(node.op)]()
        if isinstance(node, ast.Name) and node.id in ALLOWED_MATH:
            return ALLOWED_MATH[node.id]
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ALLOWED_MATH:
            function = ALLOWED_MATH[node.func.id]
            return function(*(evaluate(arg) for arg in node.args))
        raise ValueError("Only basic arithmetic and approved math functions are allowed.")

    return evaluate(tree)


def system_info():
    print("\n--- SYSTEM ---")
    print(f"OS:           {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python:       {platform.python_version()}")
    print(f"User:         {getpass.getuser()}")
    print(f"CPU cores:    {os.cpu_count()}")
    print(f"Directory:    {os.getcwd()}")
    total, used, free = shutil.disk_usage(os.getcwd())
    print(f"Disk free:    {free / (1024**3):.1f} GB / {total / (1024**3):.1f} GB")


def network_info():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = "Unavailable"
    print("\n--- NETWORK ---")
    print(f"Hostname: {hostname}")
    print(f"Local IP: {ip}")


def dice(command):
    notation = command.split(maxsplit=1)[1] if len(command.split()) > 1 else "1d6"
    try:
        count, sides = notation.lower().split("d")
        count, sides = int(count), int(sides)
        if not (1 <= count <= 20 and 2 <= sides <= 1000):
            raise ValueError
        rolls = [random.randint(1, sides) for _ in range(count)]
        print(f"Rolls: {rolls} | Total: {sum(rolls)}")
    except ValueError:
        print("Usage: roll 2d6  (1-20 dice, 2-1000 sides)")


def generate_password():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = "".join(random.SystemRandom().choice(alphabet) for _ in range(16))
    print(f"Generated password: {password}")


def handle(command):
    parts = command.split()
    if not parts:
        return True
    action = parts[0].lower()
    HISTORY.append(command)

    if action in ("exit", "quit"):
        print("NOVA shutting down. Keep building. 🚀")
        return False
    if action == "help":
        print("\n--- COMMANDS ---")
        for name, description in HELP.items():
            print(f"{name:<10} {description}")
    elif action == "about":
        print("\nNOVA is a local Python terminal playground built to practice CLI design, system information, safe parsing, and Python fundamentals.")
    elif action == "clear":
        clear()
    elif action == "time":
        print(dt.datetime.now().astimezone().strftime("%A, %d %B %Y | %H:%M:%S %Z"))
    elif action == "system":
        system_info()
    elif action == "network":
        network_info()
    elif action == "calc":
        expression = command[len(parts[0]):].strip()
        if not expression:
            print("Usage: calc 12 * (4 + 2)")
        else:
            try:
                print(f"Result: {safe_calculate(expression)}")
            except (ValueError, SyntaxError, ZeroDivisionError, OverflowError) as error:
                print(f"Calculation error: {error}")
    elif action == "roll":
        dice(command)
    elif action == "flip":
        print(random.choice(("Heads", "Tails")))
    elif action == "password":
        generate_password()
    elif action == "remember":
        if len(parts) < 3:
            print("Usage: remember key value")
        else:
            key, value = parts[1], " ".join(parts[2:])
            MEMORY[key] = value
            print(f"Memory saved: {key}")
    elif action == "recall":
        if len(parts) != 2:
            print("Usage: recall key")
        else:
            print(MEMORY.get(parts[1], "No memory found for that key."))
    elif action == "forget":
        if len(parts) != 2:
            print("Usage: forget key")
        elif MEMORY.pop(parts[1], None) is None:
            print("No memory found for that key.")
        else:
            print("Memory deleted.")
    elif action == "history":
        if not HISTORY:
            print("No commands yet.")
        else:
            for number, item in enumerate(HISTORY, 1):
                print(f"{number:>3}. {item}")
    elif action == "ls":
        for item in sorted(os.listdir(os.getcwd())):
            print(item)
    elif action == "pwd":
        print(os.getcwd())
    elif action == "cd":
        target = command[len(parts[0]):].strip() or os.path.expanduser("~")
        try:
            os.chdir(os.path.expanduser(target))
            print(f"Directory: {os.getcwd()}")
        except OSError as error:
            print(f"Cannot change directory: {error}")
    elif action == "quote":
        print(f'"{random.choice(QUOTES)}"')
    else:
        print(f"Unknown command: {action}. Type 'help'.")
    return True


def main():
    startup()
    while True:
        try:
            command = input("NOVA > ").strip()
            if not handle(command):
                break
        except KeyboardInterrupt:
            print("\nUse 'exit' to close NOVA.")
        except EOFError:
            print("\nNOVA shutting down.")
            break


if __name__ == "__main__":
    main()
