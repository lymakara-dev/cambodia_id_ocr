import cv2
import random
import numpy as np


def random_blur(img):

    if random.random() < 0.3:

        k=random.choice(
            [3,5]
        )

        img=cv2.GaussianBlur(
            img,
            (k,k),
            0
        )

    return img


def random_brightness(img):

    if random.random() < 0.5:

        alpha=random.uniform(
            0.8,
            1.2
        )

        beta=random.randint(
            -20,
            20
        )

        img=cv2.convertScaleAbs(
            img,
            alpha=alpha,
            beta=beta
        )

    return img


def random_noise(img):

    if random.random() < 0.4:

        noise=np.random.normal(

            0,
            8,
            img.shape

        ).astype(
            np.uint8
        )

        img=cv2.add(
            img,
            noise
        )

    return img


def random_rotation(img):

    if random.random() < 0.5:

        angle=random.uniform(
            -2,
            2
        )

        h,w=img.shape[:2]

        M=cv2.getRotationMatrix2D(

            (
                w//2,
                h//2
            ),

            angle,

            1
        )

        img=cv2.warpAffine(

            img,
            M,
            (w,h),

            borderMode=cv2.BORDER_REPLICATE
        )

    return img


def jpeg_artifact(img):

    if random.random()<0.5:

        quality=random.randint(
            40,
            90
        )

        encode=[

            int(
                cv2.IMWRITE_JPEG_QUALITY
            ),

            quality
        ]

        _,enc=cv2.imencode(
            ".jpg",
            img,
            encode
        )

        img=cv2.imdecode(
            enc,
            1
        )

    return img


def augment(img):

    img=random_blur(
        img
    )

    img=random_brightness(
        img
    )

    img=random_noise(
        img
    )

    img=random_rotation(
        img
    )

    img=jpeg_artifact(
        img
    )

    return img