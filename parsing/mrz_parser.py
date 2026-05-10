def parse_mrz(lines):
    if len(lines) < 3:
        return None

    line1 = lines[0]
    line2 = lines[1]
    line3 = lines[2]

    data = {}

    # line 1
    data["document_type"] = line1[0:2]
    data["country"] = line1[2:5]
    data["id_number"] = line1[5:14]

    # line 2
    data["birth_date"] = line2[0:6]
    data["sex"] = line2[7]
    data["expiry_date"] = line2[8:14]
    data["nationality"] = line2[15:18]

    # line 3
    name = line3.replace("<", " ").strip()

    parts = name.split()

    data["surname"] = parts[0] if len(parts) > 0 else ""
    data["given_name"] = " ".join(parts[1:])

    return data