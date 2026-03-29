"""Simple file-backed todo list CLI."""

from __future__ import annotations

import json
import pathlib
import textwrap
from typing import List


DATA_PATH = pathlib.Path("todos.json")


def load_tasks() -> List[dict]:
    if not DATA_PATH.exists():
        return []
    with DATA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_tasks(tasks: List[dict]) -> None:
    DATA_PATH.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def print_tasks(tasks: List[dict]) -> None:
    if not tasks:
        print("No tasks yet.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "X" if task.get("done") else " "
        print(f"[{status}] {index}. {task.get('title')}")
        if description := task.get("description"):
            wrapped = textwrap.indent(textwrap.fill(description, width=60), "    ")
            print(wrapped)


def add_task() -> None:
    title = input("Title: ").strip()
    if not title:
        print("Title is required.")
        return
    description = input("Description (optional): ").strip()
    tasks = load_tasks()
    tasks.append({"title": title, "description": description, "done": False})
    save_tasks(tasks)
    print("Task added.")


def toggle_task(done: bool) -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks to toggle.")
        return
    print_tasks(tasks)
    try:
        index = int(input("Task number: ")) - 1
        task = tasks[index]
    except (ValueError, IndexError):
        print("Invalid number.")
        return
    task["done"] = done
    save_tasks(tasks)
    print("Task updated.")


def main() -> None:
    HELP = """
    Commands:
      l - list tasks
      a - add task
      c - mark complete
      u - mark undone
      q - quit
    """
    print("Simple Todo Manager")
    while command := input("Command (h for help): ").strip().lower():
        if command == "h":
            print(HELP)
        elif command == "l":
            print_tasks(load_tasks())
        elif command == "a":
            add_task()
        elif command == "c":
            toggle_task(True)
        elif command == "u":
            toggle_task(False)
        elif command == "q":
            print("bye")
            break
        else:
            print("Unknown command. Enter h for help.")


if __name__ == "__main__":
    main()
