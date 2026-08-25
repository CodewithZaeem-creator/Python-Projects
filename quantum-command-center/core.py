from datetime import datetime

STARTED = datetime.now()


def status():
    print("\n[CORE] STATUS: ONLINE")
    print(f"[CORE] SESSION START: {STARTED:%Y-%m-%d %H:%M:%S}")
    print("[CORE] MODE: EXPLORATION")
