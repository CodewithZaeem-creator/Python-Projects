# 📚 StudyForge — CLI Flashcard Trainer

StudyForge is a small, local-first study tool built with Python. Create your own flashcards, review the cards that are due, and track your progress from the terminal.

## Features

- Create question-and-answer flashcards with topics
- Review due cards in a shuffled study session
- Rate recall as **again**, **hard**, **good**, or **easy**
- Simple spaced-review intervals (same day, 1, 3, or 7 days)
- Save cards and progress automatically in a local JSON file
- View deck statistics and delete cards
- No third-party packages, accounts, or API keys

## Run it

Requires Python 3.9 or newer.

```bash
python studyforge.py
```

## Menu

| Option | Action |
|---|---|
| A | Add a flashcard |
| S | Start a review session |
| L | List cards |
| T | View study statistics |
| D | Delete a card |
| Q | Quit |

During review, rate how well you remembered each answer:

- **again** — review again today
- **hard** — review tomorrow
- **good** — review in 3 days
- **easy** — review in 7 days

These are deliberately simple learning intervals, not a scientifically calibrated memory algorithm.

## Data and privacy

Your flashcards are stored in `cards.json` in this folder. The app works offline and does not send your study data anywhere. Back up that file if you want to keep your deck.

## Concepts practiced

Functions, lists, dictionaries, loops, input validation, JSON files, dates, randomization, and basic spaced-repetition logic.
