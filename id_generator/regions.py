from config import (
    ANNOTATION_FILE,
    WIDTH,
    HEIGHT
)


CLASS_MAP = {

    0:"appearance",
    1:"birth_address",
    2:"current_address",
    3:"dob",
    4:"expiry_date",
    5:"height",
    6:"id_number",
    7:"issue_date",
    8:"mrz",
    9:"name_en",
    10:"name_kh",
    11:"photo",
    12:"sex"
}


def load_regions():

    regions={}

    with open(
        ANNOTATION_FILE,
        encoding="utf-8"
    ) as f:

        for line in f:

            values=line.split()

            class_id=int(
                values[0]
            )

            coords=list(

                map(
                    float,
                    values[1:]
                )
            )

            points=[]

            for i in range(
                0,
                len(coords),
                2
            ):

                x=int(
                    coords[i]*
                    WIDTH
                )

                y=int(
                    coords[i+1]*
                    HEIGHT
                )

                points.append(
                    (x,y)
                )

            regions[
                CLASS_MAP[
                    class_id
                ]
            ]=points

    return regions


regions=load_regions()

print(
    list(
        regions.keys()
    )
)