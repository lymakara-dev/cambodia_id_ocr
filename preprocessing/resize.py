import cv2
import numpy as np


TARGET_WIDTH = 960
TARGET_HEIGHT = 608


def resize_with_padding(image):
    h, w = image.shape[:2]

    scale = min(
        TARGET_WIDTH / w,
        TARGET_HEIGHT / h
    )

    new_w = int(w * scale)
    new_h = int(h * scale)

    resized = cv2.resize(
        image,
        (new_w, new_h)
    )

    canvas = np.zeros(
        (
            TARGET_HEIGHT,
            TARGET_WIDTH,
            3
        ),
        dtype=np.uint8
    )

    x_offset = (TARGET_WIDTH - new_w) // 2
    y_offset = (TARGET_HEIGHT - new_h) // 2

    canvas[
        y_offset:y_offset + new_h,
        x_offset:x_offset + new_w
    ] = resized

    return canvas