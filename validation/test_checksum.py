from checksum import validate_checksum

value = "750511"
checksum_digit = "3"

result = validate_checksum(
    value,
    checksum_digit
)

print(result)