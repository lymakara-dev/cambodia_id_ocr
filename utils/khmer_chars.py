def load_khmer_chars():

    with open(
        "data/dictionaries/khmer_chars.txt",
        "r",
        encoding="utf-8"
    ) as f:

        chars = [
            line.strip()
            for line in f.readlines()
            if line.strip()
        ]

    return set(chars)


KHMER_CHARS = load_khmer_chars()