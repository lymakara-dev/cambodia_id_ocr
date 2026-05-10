from mrz_parser import parse_mrz

mrz_lines = [
    "IDKHM1806714117<<<",
    "7505113M3401088KHM<<8",
    "CHHAY<<SETHY<<<<<<<<<<<<<<<<<"
]

data = parse_mrz(mrz_lines)

print(data)