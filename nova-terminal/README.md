# 🤖 NOVA Terminal

A futuristic command-line assistant built entirely with Python's standard library.

NOVA is designed as a learning project that combines multiple Python concepts into one interactive terminal experience.

## ⚡ Features

- 🤖 Futuristic startup sequence and ASCII interface
- 🧮 Safe calculator using Python's AST parser instead of raw `eval()`
- 💻 System information
- 🌐 Local network information
- 📁 File and directory navigation
- 🧠 Session memory with `remember`, `recall`, and `forget`
- 📜 Command history
- 🎲 Dice roller such as `roll 2d6`
- 🪙 Coin flip
- 🔐 Random password generation
- 🕐 Real-time date and time
- 💬 Random motivational quotes
- 🧹 Terminal clearing
- 📦 Zero third-party dependencies

## ▶️ Run It

```bash
python nova.py
```

## 🕹️ Commands

```text
help                 Show all commands
about                About NOVA
time                 Current date and time
system               System information
network              Local network information
calc 12 * (4 + 2)    Calculator
roll 2d6             Roll dice
flip                 Flip a coin
password             Generate a password
remember name Zaeem  Save information
recall name          Read saved information
forget name          Delete saved information
history              Command history
ls                   List files
pwd                  Current directory
cd folder            Change directory
quote                Random quote
clear                Clear terminal
exit                 Close NOVA
```

## 🧠 What This Project Teaches

- Functions and modular program design
- Dictionaries and lists
- Loops and conditionals
- Exception handling
- File-system navigation
- `os`, `platform`, `socket`, and `shutil`
- Random data generation
- Date and time handling
- Parsing command-line input
- Python's `ast` module
- Building an interactive CLI application

## 🔐 Security Note

The calculator intentionally parses expressions with `ast` and only permits a small set of arithmetic operations and math functions. It does **not** pass arbitrary user input directly into `eval()`.

The password generator is for learning and general local use. Do not treat it as a replacement for a dedicated password manager's secure generation and storage features.

## 🚀 Future Ideas

- Persistent encrypted memory
- Plugin system for new commands
- Live weather integration
- GitHub command integration
- Local AI integration
- Configurable themes
- Command autocomplete
- Task/reminder system
