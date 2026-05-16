import random

from services.dictionary_loader import (
    load_dictionary
)

APPEARANCES = load_dictionary(
    "appearance.txt"
)


def random_appearance():

    appearance = random.choice(
        APPEARANCES
    )

    return {

        "appearance":
        appearance
    }