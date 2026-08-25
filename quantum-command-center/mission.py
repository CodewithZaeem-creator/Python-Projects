MISSIONS = [
    "Build something you don't understand yet.",
    "Turn one bug into one lesson.",
    "Read the error message before changing the code.",
    "Ship a small feature today.",
    "Explain your project without looking at the code.",
]


def random_mission():
    import random
    return random.choice(MISSIONS)
