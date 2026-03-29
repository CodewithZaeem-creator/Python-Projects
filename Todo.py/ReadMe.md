 # ✅ Simple Todo Manager

A lightweight command-line todo app built in Python. Your tasks are saved to a `todos.json` file so they stick around even after you close the terminal — no database, no sign-up, no fuss.

> My third Python project — learning how to read/write files and build a real CLI tool. 🐍

---

## 🎮 Demo

```
Simple Todo Manager
Command (h for help): h

    Commands:
      l - list tasks
      a - add task
      c - mark complete
      u - mark undone
      q - quit

Command (h for help): a
Title: Buy groceries
Description (optional): Milk, eggs, bread
Task added.

Command (h for help): l
[ ] 1. Buy groceries
    Milk, eggs, bread

Command (h for help): c
[ ] 1. Buy groceries
Task number: 1
Task updated.

Command (h for help): l
[X] 1. Buy groceries
    Milk, eggs, bread
```

---

## ✨ Features

- ➕ Add tasks with a title and optional description
- 📋 List all tasks with their completion status
- ✅ Mark tasks as complete or undo them
- 💾 Tasks are saved to `todos.json` — they persist between sessions
- 🪶 Zero dependencies — uses only Python's built-in libraries
- ⌨️ Fast single-letter commands — no typing long words

---

## 🚀 Getting Started

### 1. Make sure Python is installed

```bash
python --version
```

Python 3.9 or higher recommended. Download from [python.org](https://www.python.org/downloads/) if needed.

### 2. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Python-Projects.git
cd Python-Projects/todo
```

### 3. Run the app

```bash
python todo.py
```

No `pip install` needed — this project uses only Python's built-in libraries. ✅

---

## 📖 Commands

| Command | What it does |
|---|---|
| `h` | Show the help menu |
| `l` | List all tasks |
| `a` | Add a new task |
| `c` | Mark a task as complete `[X]` |
| `u` | Mark a task as undone `[ ]` |
| `q` | Quit the app |

---

## 📁 Project Structure

```
todo/
│
├── todo.py       # All the app logic
├── todos.json    # Auto-created when you add your first task
└── README.md     # This file
```

> **Note:** `todos.json` is created automatically the first time you add a task. You don't need to create it yourself.

---

## 🧠 How It Works

```
You enter a command
        ↓
App reads todos.json into a Python list
        ↓
Your action runs (add / list / toggle)
        ↓
Updated list is saved back to todos.json
        ↓
Tasks are there next time you open the app 💾
```

The tasks are stored in JSON format like this:

```json
[
  {
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "done": false
  }
]
```

---

## 🧩 What Makes This Code Interesting

This project uses some Python patterns worth knowing about:

- **`pathlib`** — a modern way to work with file paths, cleaner than the old `os.path`
- **`json`** — built-in library for saving and loading structured data
- **`textwrap`** — automatically wraps long descriptions so they display neatly in the terminal
- **Type hints** like `List[dict]` — makes the code easier to read and understand
- **`if __name__ == "__main__"`** — best practice so the app only runs when you call it directly

---

## 💡 Ideas for What to Add Next

- 🗑️ **Delete tasks** — remove a task by number
- 📅 **Due dates** — add a deadline to each task
- 🔍 **Search** — filter tasks by keyword
- 🎨 **Colours** — use the `colorama` library to make completed tasks green
- 🖥️ **GUI version** — rebuild it with Tkinter for a clickable interface

---

## 🌱 What I Learned

- How to read and write JSON files in Python
- How to use `pathlib` to handle files the modern way
- How to build a command-line interface with a command loop
- How to structure a project with separate functions for each job
- How persistent storage works — saving data so it survives closing the app

---

## 📄 License

MIT License — free to use, modify, and share.

---

*Made with ❤️ as part of my Python learning journey. If you found this useful, leave a ⭐ on GitHub!*   