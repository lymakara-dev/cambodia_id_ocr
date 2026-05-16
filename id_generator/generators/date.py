import random


KHMER_DIGITS={

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

        for c in str(
            value
        )
    )


def random_kh_date(
    start_year,
    end_year
):

    day=random.randint(
        1,
        28
    )

    month=random.randint(
        1,
        12
    )

    year=random.randint(
        start_year,
        end_year
    )

    day=f"{day:02}"
    month=f"{month:02}"

    day=to_khmer_number(
        day
    )

    month=to_khmer_number(
        month
    )

    year=to_khmer_number(
        year
    )

    return (

        f"{day}."
        f"{month}."
        f"{year}"
    )


def random_dates():

    issue=random.randint(
        2015,
        2025
    )

    expiry=issue+10

    return {

        "dob":

        random_kh_date(
            1980,
            2005
        ),

        "issue_date":

        random_kh_date(
            issue,
            issue
        ),

        "expiry_date":

        random_kh_date(
            expiry,
            expiry
        )
    }