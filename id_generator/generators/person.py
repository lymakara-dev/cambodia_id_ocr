import random

from services.dictionary_loader import (
    load_dictionary
)


KH_FIRST = load_dictionary(
    "khmer_first_names.txt"
)

EN_FIRST = load_dictionary(
    "english_first_names.txt"
)

KH_LAST = load_dictionary(
    "khmer_last_names.txt"
)

EN_LAST = load_dictionary(
    "english_last_names.txt"
)


KHMER_DIGITS = {

    "0":"០",
    "1":"១",
    "2":"២",
    "3":"៣",
    "4":"៤",
    "5":"៥",
    "6":"៦",
    "7":"៧",
    "8":"៨",
    "9":"៩"
}


def to_khmer_number(value):

    return "".join(

        KHMER_DIGITS.get(
            c,
            c
        )

        for c in str(value)
    )


def random_id():

    return str(

        random.randint(
            100000000,
            999999999
        )
    )


def random_height():

    value=random.randint(
        145,
        190
    )

    return (

        f"{to_khmer_number(value)} "
        f"ស.ម"
    )


def random_person():

    first_index=random.randint(

        0,
        len(KH_FIRST)-1
    )

    last_index=random.randint(

        0,
        len(KH_LAST)-1
    )


    kh_first=KH_FIRST[
        first_index
    ]

    en_first=EN_FIRST[
        first_index
    ]


    kh_last=KH_LAST[
        last_index
    ]

    en_last=EN_LAST[
        last_index
    ]


    kh_name=(

        f"{kh_last} "
        f"{kh_first}"
    )

    en_name=(

        f"{en_last} "
        f"{en_first}"

    ).upper()


    sex=random.choice(

        [
            "ប្រុស",
            "ស្រី"
        ]
    )


    return {

        "id_number":
        random_id(),

        "name_kh":
        kh_name,

        "name_en":
        en_name,

        "sex":
        sex,

        "height":
        random_height()
    }