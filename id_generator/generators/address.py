import random

from services.dictionary_loader import (
    load_dictionary
)

COMMUNES=load_dictionary(
    "communes.txt"
)

DISTRICTS=load_dictionary(
    "districts.txt"
)

PROVINCES=load_dictionary(
    "provinces.txt"
)

VILLAGES=load_dictionary(
    "villages.txt"
)


def random_address():

    village=random.choice(
        VILLAGES
    )

    commune=random.choice(
        COMMUNES
    )

    district=random.choice(
        DISTRICTS
    )

    province=random.choice(
        PROVINCES
    )

    house=random.randint(
        1,
        999
    )

    street=random.randint(
        1,
        999
    )

    return {

        "birth_address":

        f"ឃុំ{commune} "
        f"ស្រុក{district} "
        f"ខេត្ត{province}",


        "current_address":

        f"ផ្ទះ{house} "
        f"ផ្លូវ{street} "
        f"ភូមិ{village}\n"

        f"សង្កាត់{commune} "
        f"ខណ្ឌ{district} "
        f"ភ្នំពេញ"
    }