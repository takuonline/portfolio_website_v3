from flask import Flask, render_template, session, redirect, url_for
import numpy as np
from skimage import io
import cv2, os
from difflib import get_close_matches


def detect_and_blur_plate(file_location):
    dirname = os.path.dirname(__file__)
    static = os.path.join(dirname, "..", "static")
    casc_path = os.path.join(static, "haarcascades/haarcascade_frontalface_alt2.xml")

    casc = cv2.CascadeClassifier(casc_path)

    try:
        img = io.imread(file_location)
    except:
        print("could not find pic")
    name = str(str(file_location).split("/")[-1])  # file name

    try:
        no_image = False
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        rect_measures = casc.detectMultiScale(img, minNeighbors=5)
        number = str(len(rect_measures))
        for x, y, w, h in rect_measures:

            to_blur = img[y : y + h, x : x + w]
            font = cv2.FONT_HERSHEY_COMPLEX
            blurred = cv2.medianBlur(to_blur, 51)
            try:
                img[y : y + h, x : x + w] = blurred
                cv2.putText(
                    img, "Face", (img.shape[0], 0), font, 1, [255, 0, 0], 1, cv2.LINE_AA
                )
            except UnboundLocalError:
                print("Sorry could not find a face in the image")
        path = "website//static//" + name

        try:
            cv2.imwrite(path, img)
        except cv2.error:
            name = "error"

    except UnboundLocalError:
        name = "error"
        print("\n\n\n\n\n Unbound error print\n\n\n\n\n\n\n")
    return name
