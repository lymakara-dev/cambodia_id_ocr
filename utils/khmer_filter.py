from utils.khmer_chars import (
    KHMER_CHARS
)


def filter_khmer_text(text):

    result = ""

    for char in text:

        if (
            char in KHMER_CHARS
            or char == " "
        ):

            result += char

    return result.strip()