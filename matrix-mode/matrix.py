"""Matrix Mode - a terminal rain animation using only the Python standard library."""

import os
import random
import shutil
import time

CHARS = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def run(duration=12):
    columns = max(20, shutil.get_terminal_size((80, 24)).columns)
    rows = max(8, shutil.get_terminal_size((80, 24)).lines)
    drops = [random.randint(-rows, 0) for _ in range(columns)]
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            output = []
            for row in range(rows - 1):
                line = []
                for column in range(columns):
                    distance = row - drops[column]
                    if 0 <= distance <= 5:
                        line.append(random.choice(CHARS))
                    else:
                        line.append(" ")
                output.append("".join(line))

            clear()
            print("\n".join(output))

            for column in range(columns):
                if drops[column] > rows + random.randint(0, 10):
                    drops[column] = random.randint(-10, 0)
                else:
                    drops[column] += 1

            time.sleep(0.06)
    except KeyboardInterrupt:
        pass
    finally:
        clear()
        print("MATRIX MODE OFF")


def main():
    clear()
    print("MATRIX MODE")
    print("Terminal rain will run for 12 seconds.")
    print("Press Ctrl+C to stop early.")
    time.sleep(1)
    run()


if __name__ == "__main__":
    main()
