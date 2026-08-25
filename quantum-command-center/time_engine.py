from datetime import datetime


def show_time():
    now = datetime.now()
    print(f"\nTEMPORAL SYNC: {now:%A, %d %B %Y}")
    print(f"LOCAL CLOCK:   {now:%H:%M:%S}")
