import os

from config import DICT_DIR


def load_dictionary(file_name):

    path = os.path.join(
        DICT_DIR,
        file_name
    )

    if not os.path.exists(path):

        raise FileNotFoundError(
            f"Dictionary not found: {path}"
        )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        values = [

            line.strip()

            for line in f

            if line.strip()
        ]

    return values