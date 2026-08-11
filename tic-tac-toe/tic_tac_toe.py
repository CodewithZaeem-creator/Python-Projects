import random


def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    return any(all(board[index] == player for index in combo) for combo in winning_combinations)


def board_full(board):
    return all(cell in ("X", "O") for cell in board)


def get_player_move(board):
    while True:
        move = input("Choose a position (1-9): ").strip()

        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        index = int(move) - 1
        if board[index] in ("X", "O"):
            print("That position is already taken.")
            continue

        return index


def get_computer_move(board):
    available = [index for index, cell in enumerate(board) if cell not in ("X", "O")]

    # Win if possible.
    for index in available:
        test_board = board.copy()
        test_board[index] = "O"
        if check_winner(test_board, "O"):
            return index

    # Block the player if necessary.
    for index in available:
        test_board = board.copy()
        test_board[index] = "X"
        if check_winner(test_board, "X"):
            return index

    # Prefer the center, then corners, then any remaining position.
    if 4 in available:
        return 4

    corners = [index for index in (0, 2, 6, 8) if index in available]
    if corners:
        return random.choice(corners)

    return random.choice(available)


def play_game():
    board = [str(number) for number in range(1, 10)]
    current_player = "X"

    print("\n=== TIC-TAC-TOE ===")
    print("You are X. The computer is O.")
    print("Use the numbers on the board to choose a position.")

    while True:
        display_board(board)

        if current_player == "X":
            move = get_player_move(board)
        else:
            print("Computer is choosing...")
            move = get_computer_move(board)

        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            if current_player == "X":
                print("You win! 🎉")
            else:
                print("Computer wins! 🤖")
            break

        if board_full(board):
            display_board(board)
            print("It's a draw! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
