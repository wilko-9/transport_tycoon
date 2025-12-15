import random


def generate_town_name():
    prefixes = [
        "Oak", "River", "Stone", "Pine", "Clear", "Red", "Iron", "Silver"
    ]

    suffixes = [
        "ville", "ton", "ford", "wood", "field", "bury", "crest", "haven"
    ]

    return random.choice(prefixes) + random.choice(suffixes)
