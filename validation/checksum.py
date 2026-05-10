def char_value(char):
    if char.isdigit():
        return int(char)

    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 10

    if char == '<':
        return 0

    return 0


def calculate_checksum(value):
    weights = [7, 3, 1]

    total = 0

    for i, char in enumerate(value):
        total += char_value(char) * weights[i % 3]

    return total % 10


def validate_checksum(value, checksum_digit):
    expected = calculate_checksum(value)

    return expected == int(checksum_digit)