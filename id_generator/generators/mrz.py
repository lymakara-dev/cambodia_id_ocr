import re


KHMER_TO_EN = {

    "០":"0",
    "១":"1",
    "២":"2",
    "៣":"3",
    "៤":"4",
    "៥":"5",
    "៦":"6",
    "៧":"7",
    "៨":"8",
    "៩":"9"
}


def khmer_to_english(text):

    return "".join(

        KHMER_TO_EN.get(
            c,
            c
        )

        for c in text
    )


def clean(text):

    text=text.upper()

    text=re.sub(

        r"[^A-Z0-9]",

        "<",

        text
    )

    return text


def pad(
    text,
    length=30
):

    return text.ljust(
        length,
        "<"
    )


def convert_date_for_mrz(date):

    # input:
    # ០៣.០៩.២០០៤

    date=khmer_to_english(
        date
    )

    day,month,year=(
        date.split(".")
    )

    year=year[-2:]

    return (

        day+
        month+
        year
    )


def create_mrz(data):

    id_number=data[
        "id_number"
    ]

    sex=data[
        "sex"
    ]

    if sex=="ប្រុស":

        sex="M"

    else:

        sex="F"


    dob=convert_date_for_mrz(

        data["dob"]
    )

    expiry=convert_date_for_mrz(

        data["expiry_date"]
    )


    names=data[
        "name_en"
    ].split()


    last_name=clean(
        names[0]
    )

    first_name=clean(

        " ".join(
            names[1:]
        )
    )


    line1=pad(

        f"IDKHM{id_number}"

    )


    line2=pad(

        f"{dob}"
        f"{sex}"
        f"{expiry}"
        f"KHM0"

    )


    line3=pad(

        f"{last_name}"
        f"<<"
        f"{first_name}"

    )


    return (

        line1
        + "\n"
        + line2
        + "\n"
        + line3
    )