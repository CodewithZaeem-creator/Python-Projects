# ✂️ Stone Paper Scissor Game

A classic Stone Paper Scissor game built in Python. Play against the computer right in your terminal — one command and you're in!

> My second Python project — learning conditionals, random choices, and string handling. 🐍

---

## 🎮 Demo

```
Welcome to Stone Paper Scissor game
Enter stone, paper or scissor: stone
computer: scissor
You win! 🎉
```

```
Welcome to Stone Paper Scissor game
Enter stone, paper or scissor: paper
computer: paper
this is tie
```

---

## ✨ Features

- 🤖 Computer picks randomly every round — impossible to predict
- ⌨️ Case-insensitive input — type `Stone`, `STONE`, or `stone`, all work
- 🏆 Detects all outcomes — win, lose, and tie
- ⚠️ Friendly message for invalid input
- 🪶 Zero dependencies — only uses Python's built-in `random` library

---

## 🚀 Getting Started

### 1. Make sure Python is installed

```bash
python --version
```

Download from [python.org](https://www.python.org/downloads/) if needed.

### 2. Clone the repository

```bash
git clone https://github.com/CodewithZaeem-creator/Python-Projects.git
cd Python-Projects/stone-paper-scissor
```

### 3. Run the game

```bash
python stone_paper_scissor.py
```

No `pip install` needed — zero external libraries. ✅

---

## 📜 Game Rules

| Your Choice | Computer Choice | Result |
|---|---|---|
| ✊ Stone | ✂️ Scissor | You win |
| 📄 Paper | ✊ Stone | You win |
| ✂️ Scissor | 📄 Paper | You win |
| Anything | Same | Tie |
| ✂️ Scissor | ✊ Stone | Computer wins |
| ✊ Stone | 📄 Paper | Computer wins |
| 📄 Paper | ✂️ Scissor | Computer wins |

---

## 🧠 How It Works

```
You type your choice (stone / paper / scissor)
                ↓
      .lower() makes it case-insensitive
                ↓
   Computer picks randomly from the list
                ↓
   if / elif checks all possible outcomes
                ↓
        Winner is announced! 🏆
```

---

## 📁 Project Structure

```
stone-paper-scissor/
│
├── stone_paper_scissor.py   # All the game logic
└── README.md                # This file
```

---

## 🐛 Bugs I Fixed Along the Way

This was my first real debugging experience — and I learned a lot from it:

- **`random.choices()`** returns a list like `['stone']` not a plain string — switching to `random.choice()` (no s) fixed it
- **Capitalisation mismatch** — my choices list had `"Stone"` but `.lower()` on user input gave `"stone"` so comparisons never matched — fixed by making the list all lowercase too
- **Tie condition was broken** silently because of the same capitalisation bug above

Reading error output carefully and understanding *why* something breaks is the real skill — not just fixing it.

---

## 💡 Ideas for What to Add Next

- 🔁 **Play again loop** — ask the user for another round without restarting
- 🏆 **Score tracker** — keep count of wins, losses, and ties
- 🖥️ **Tkinter GUI** — buttons for each choice instead of typing
- 🦎 **Rock Paper Scissors Lizard Spock** — the expanded version from The Big Bang Theory!

---

## 🌱 What I Learned

- How `random.choice()` works and why `random.choices()` is different
- Why string capitalisation matters — `"Stone"` and `"stone"` are not equal in Python
- How `.lower()` makes user input consistent and safe to compare
- How to cover all game outcomes cleanly with `if / elif / else`
- How to debug by reading errors carefully and tracing the logic

---

## 📄 License

MIT License — free to use, modify, and share.

---

*Made with ❤️ as part of my Python learning journey. If you liked it, leave a ⭐ on GitHub!*
