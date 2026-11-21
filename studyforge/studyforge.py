"""StudyForge: a local-first CLI flashcard and study tracker.

Uses only the Python standard library. Cards are stored in cards.json beside
this script. Ratings: again, hard, good, easy.
"""
from __future__ import annotations

import json
import random
from datetime import date, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).with_name("cards.json")
BOXES = {"again": 1, "hard": 1, "good": 2, "easy": 3}


def load_cards() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: cards.json could not be read. Starting with an empty deck.")
        return []


def save_cards(cards: list[dict]) -> None:
    DATA_FILE.write_text(json.dumps(cards, indent=2, ensure_ascii=False), encoding="utf-8")


def add_card(cards: list[dict]) -> None:
    question = input("Question: ").strip()
    if not question:
        print("Question cannot be empty.")
        return
    answer = input("Answer: ").strip()
    if not answer:
        print("Answer cannot be empty.")
        return
    topic = input("Topic (optional): ").strip() or "General"
    cards.append({
        "question": question, "answer": answer, "topic": topic,
        "due": date.today().isoformat(), "box": 1, "reviews": 0,
        "correct": 0, "created": date.today().isoformat(),
    })
    save_cards(cards)
    print("Card added.")


def review_session(cards: list[dict]) -> None:
    today = date.today()
    due = [c for c in cards if c.get("due", "") <= today.isoformat()]
    if not due:
        print("No cards due today. Add a card or come back later!")
        return
    random.shuffle(due)
    print(f"\nStudy session: {len(due)} card(s) due. Type q to stop.\n")
    for card in due:
        print(f"TOPIC: {card.get('topic', 'General')}")
        print(f"Q: {card['question']}")
        command = input("Press Enter to reveal, or q to quit: ").strip().lower()
        if command == "q":
            break
        print(f"A: {card['answer']}")
        rating = input("How well did you know it? [again/hard/good/easy]: ").strip().lower()
        while rating not in BOXES:
            rating = input("Choose again, hard, good, or easy: ").strip().lower()
        box = BOXES[rating]
        card["box"] = box
        card["reviews"] = int(card.get("reviews", 0)) + 1
        if rating in ("good", "easy"):
            card["correct"] = int(card.get("correct", 0)) + 1
        # A small, transparent spaced-review schedule (days).
        intervals = {1: 1, 2: 3, 3: 7}
        if rating == "hard":
            days = 1
        elif rating == "again":
            days = 0
        else:
            days = intervals[box]
        card["due"] = (today + timedelta(days=days)).isoformat()
        print(f"Next review: {card['due']}\n")
        save_cards(cards)
    print("Session saved.")


def list_cards(cards: list[dict]) -> None:
    if not cards:
        print("Your deck is empty. Add your first card!")
        return
    for number, card in enumerate(cards, 1):
        print(f"{number:>3}. [{card.get('topic', 'General')}] {card['question']}  (due {card.get('due', 'unknown')})")


def show_stats(cards: list[dict]) -> None:
    reviews = sum(int(c.get("reviews", 0)) for c in cards)
    correct = sum(int(c.get("correct", 0)) for c in cards)
    due = sum(c.get("due", "") <= date.today().isoformat() for c in cards)
    topics = len({c.get("topic", "General") for c in cards})
    rate = (correct / reviews * 100) if reviews else 0
    print("\n--- STUDY STATS ---")
    print(f"Cards: {len(cards)} | Topics: {topics} | Reviews: {reviews}")
    print(f"Due now: {due} | Good/easy rate: {rate:.1f}%")


def delete_card(cards: list[dict]) -> None:
    list_cards(cards)
    if not cards:
        return
    raw = input("Card number to delete (or Enter to cancel): ").strip()
    if not raw:
        return
    if not raw.isdigit() or not 1 <= int(raw) <= len(cards):
        print("Invalid card number.")
        return
    removed = cards.pop(int(raw) - 1)
    save_cards(cards)
    print(f"Deleted: {removed['question']}")


def main() -> None:
    cards = load_cards()
    print("\n╔══════════════════════════════════╗")
    print("║       STUDYFORGE  /  CLI         ║")
    print("║   Build knowledge, one card at a time ║")
    print("╚══════════════════════════════════╝")
    while True:
        print("\n[A]dd  [S]tudy  [L]ist  [T]stats  [D]elete  [Q]uit")
        choice = input("studyforge> ").strip().lower()
        if choice in ("a", "add"):
            add_card(cards)
        elif choice in ("s", "study"):
            review_session(cards)
        elif choice in ("l", "list"):
            list_cards(cards)
        elif choice in ("t", "stats", "tstats"):
            show_stats(cards)
        elif choice in ("d", "delete"):
            delete_card(cards)
        elif choice in ("q", "quit", "exit"):
            print("Keep learning. See you next session!")
            break
        else:
            print("Unknown command. Choose A, S, L, T, D, or Q.")


if __name__ == "__main__":
    main()
