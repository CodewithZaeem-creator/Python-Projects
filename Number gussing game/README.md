🔢 Number Guessing Game
A fun command-line game where you try to guess a secret number between 1 and 100. The computer tells you if you're too high or too low until you crack it — then asks if you want to play again!

My fourth Python project — learning loops, error handling, and functions. 🐍


🎮 Demo
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
Your guess: 50
Too low. Try again.
Your guess: 75
Too high. Try again.
Your guess: 63
Too low. Try again.
Your guess: 69
Well done! You guessed the number in 4 attempts.

Play again? (y/n): n
Thanks for playing!

✨ Features

🎲 Random number generated between 1 and 100 every round
📈 Tells you if your guess is too high or too low
🔢 Counts how many attempts it took you to win
🔁 Play again without restarting the program
🛡️ Handles bad input — letters, symbols, empty guesses all caught gracefully
🪶 Zero dependencies — uses only Python's built-in libraries


🚀 Getting Started
1. Make sure Python is installed
bashpython --version
Python 3.9 or higher recommended. Download from python.org if needed.
2. Clone the repository
bashgit clone https://github.com/CodewithZaeem-creator/Python-Projects.git
cd Python-Projects/number-guessing-game
3. Run the game
bashpython guessing_game.py
No pip install needed — only uses Python's built-in random library. ✅

🧠 How It Works
Game starts — computer picks a random number (1–100)
                        ↓
            You type your guess
                        ↓
         Is it a valid number?
          /                  \
        No                   Yes
   Show error              attempts + 1
   Try again                   ↓
                     Too low / Too high / Correct?
                      ↓          ↓           ↓
                  "Too low"  "Too high"   "Well done!"
                  Try again   Try again       ↓
                                        Play again? (y/n)

🧩 What Makes This Code Interesting

random.randint(1, 100) — generates a fresh secret number every round
try / except ValueError — catches when the user types letters instead of numbers, no crash
while True loop — keeps the game running until the correct guess
Two separate functions — play_game() handles one round, main() handles replaying — clean separation of responsibilities
if __name__ == "__main__" — best practice so the game only runs when called directly


💡 Ideas for What to Add Next

🏆 Difficulty levels — Easy (1–50), Medium (1–100), Hard (1–500)
⏱️ Timer — track how long it takes to guess
🥇 High score tracker — save your best attempt count to a file
💡 Hint system — after 5 wrong guesses, give a clue
🖥️ Tkinter GUI — add a window with buttons and a progress bar


📁 Project Structure
number-guessing-game/
│
├── guessing_game.py   # All the game logic
└── README.md          # This file

🌱 What I Learned

How to generate random numbers with the random library
How to use try/except to handle invalid user input without crashing
How to use while True loops and break to control game flow
How to separate code into clean focused functions
How to count attempts and display them to the user


📄 License
MIT License — free to use, modify, and share.

Made with ❤️ as part of my Python learning journey. If you enjoyed it, leave a ⭐ on GitHub!