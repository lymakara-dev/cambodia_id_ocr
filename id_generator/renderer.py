from PIL import (
    ImageDraw
)

from regions import regions

from helpers import (
    polygon_to_bbox
)

from fonts import *

FIELD_OFFSET = {

    "name_kh": (0,0),

    "name_en": (0,0),

    "dob": (0,-10),

    "sex": (0,-10),

    "height": (0,-10),

    "birth_address": (0,-10),

    "appearance": (0,-10),

    "issue_date": (0,-10),

    "expiry_date": (0,-10),

    "current_address": (130,-50),

    "id_number": (30,0),

    "mrz": (30,30)
}


def get_font(field):

    if field=="name_kh":

        return font_name_kh

    elif field=="name_en":

        return font_en

    elif field=="mrz":

        return font_mrz

    else:

        return font_kh_big

def draw_bold_text(
    draw,
    position,
    text,
    font,
    fill,
    thickness=1
):

    x,y = position

    offsets = [

        (0,0),

        (thickness,0),
        (-thickness,0),

        (0,thickness),
        (0,-thickness)
    ]

    for dx,dy in offsets:

        draw.multiline_text(

            (
                x+dx,
                y+dy
            ),

            text,

            font=font,

            fill=fill,

            spacing=10
        )

def draw_spaced_text(
    draw,
    position,
    text,
    font,
    fill,
    char_spacing=3,
    thickness=1
):

    x, y = position

    for char in str(text):

        offsets = [

            (0,0),

            (thickness,0),
            (-thickness,0),

            (0,thickness),
            (0,-thickness)
        ]

        for dx, dy in offsets:

            draw.text(

                (
                    x + dx,
                    y + dy
                ),

                char,

                font=font,

                fill=fill
            )

        bbox = draw.textbbox(

            (x, y),

            char,

            font=font
        )

        width = bbox[2] - bbox[0]

        x += width + char_spacing

def draw_mrz(
    draw,
    position,
    text,
    font,
    fill,
    char_spacing=2,
    line_spacing=32,
    thickness=1
):

    x0, y0 = position

    lines = text.split("\n")

    offsets = [

        (0,0),

        (thickness,0),
        (-thickness,0),

        (0,thickness),
        (0,-thickness)
    ]

    for line_index, line in enumerate(lines):

        x = x0

        y = y0 + (line_index * line_spacing)

        for char in line:

            for dx, dy in offsets:

                draw.text(

                    (
                        x + dx,
                        y + dy
                    ),

                    char,

                    font=font,

                    fill=fill
                )

            bbox = draw.textbbox(

                (x, y),

                char,

                font=font
            )

            width = bbox[2] - bbox[0]

            x += width + char_spacing

def draw_fields(
    image,
    data
):

    draw = ImageDraw.Draw(
        image
    )

    for field, value in data.items():

        if field not in regions:

            print(
                field,
                field in regions
            )

            continue

        x1, y1, x2, y2 = (

            polygon_to_bbox(
                regions[field]
            )
        )

        dx, dy = FIELD_OFFSET.get(

            field,

            (0,0)
        )

        font = get_font(
            field
        )

        position = (

            x1 + dx,
            y1 + dy
        )

        if field == "name_kh":

            draw.multiline_text(

                position,

                str(value),

                font=font,

                fill=(20,20,20),

                spacing=10
            )

        elif field == "id_number":

            draw_spaced_text(

                draw=draw,

                position=position,

                text=str(value),

                font=font,

                fill=(20,20,20),

                char_spacing=4,
                
                thickness=1
            )
        
        elif field == "mrz":

            draw_mrz(

                draw=draw,

                position=position,

                text=str(value),

                font=font,

                fill=(20,20,20),

                char_spacing=10,

                line_spacing=60,

                thickness=1
            )

        else:

            draw_bold_text(

                draw=draw,

                position=position,

                text=str(value),

                font=font,

                fill=(20,20,20),

                thickness=1
            )

    return image