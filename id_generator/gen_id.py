import json
import uuid
import cv2
import numpy as np

from PIL import Image

from config import (
    COUNT,
    WIDTH,
    HEIGHT,
    OUTPUT_DIR,
    TEMPLATE_IMAGE,
    LABEL_FILE
)

from renderer import (
    draw_fields
)

from generators.person import *
from generators.address import *
from generators.date import *
from generators.appearance import *
from generators.mrz import *

from services.augmentation import (
    augment
)


def build_data():

    person=random_person()

    address=random_address()

    dates=random_dates()

    appearance=random_appearance()

    data={

        **person,

        **address,

        **dates,

        **appearance
    }

    data["mrz"]=create_mrz(
        data
    )

    return data


def main():

    labels=[]

    template=cv2.imread(
        str(
            TEMPLATE_IMAGE
        )
    )

    if template is None:

        raise Exception(
            "Cannot load template"
        )

    template=cv2.resize(

        template,

        (
            WIDTH,
            HEIGHT
        )
    )

    for i in range(
        COUNT
    ):

        data=build_data()

        image=Image.fromarray(

            cv2.cvtColor(

                template,

                cv2.COLOR_BGR2RGB
            )
        )

        image=draw_fields(

            image,
            data
        )

        img=np.array(
            image
        )

        img=cv2.cvtColor(

            img,

            cv2.COLOR_RGB2BGR
        )

        # img=augment(
        #     img
        # )

        uid=str(
            uuid.uuid4()
        )

        filename=(
            f"{uid}.png"
        )

        cv2.imwrite(

            str(
                OUTPUT_DIR/
                filename
            ),

            img
        )

        labels.append({

            "image":
            filename,

            **data
        })


    with open(

        LABEL_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            labels,

            f,

            ensure_ascii=False,

            indent=4
        )


if __name__=="__main__":

    main()