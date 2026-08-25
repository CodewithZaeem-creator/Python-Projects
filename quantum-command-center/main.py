from banner import show_banner
from core import status
from diagnostics import run as diagnostics
from time_engine import show_time
from secure_calculator import calculate
from memory import Memory
from mission import random_mission


def main():
    show_banner()
    memory = Memory()
    print("Type HELP for commands. Type EXIT to leave.\n")
    while True:
        try:
            command = input("QCORE > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nCORE SHUTDOWN.")
            break
        if not command:
            continue
        parts = command.split(maxsplit=2)
        action = parts[0].lower()
        if action == "help":
            print("status | diagnostics | time | calc EXPR | mission | remember KEY VALUE | recall KEY | memory | exit")
        elif action == "status":
            status()
        elif action == "diagnostics":
            diagnostics()
        elif action == "time":
            show_time()
        elif action == "calc" and len(parts) > 1:
            try: print("RESULT:", calculate(command[5:]))
            except ValueError as exc: print("ERROR:", exc)
        elif action == "mission":
            print("MISSION:", random_mission())
        elif action == "remember" and len(parts) == 3:
            memory.remember(parts[1], parts[2]); print("Memory stored.")
        elif action == "recall" and len(parts) > 1:
            print(memory.recall(parts[1]))
        elif action == "memory":
            memory.show()
        elif action == "exit":
            print("Quantum Core shutting down...")
            break
        else:
            print("Unknown command. Type HELP.")


if __name__ == "__main__":
    main()
