import cv2
import numpy as np


def preprocess_img(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurr = cv2.GaussianBlur(img_gray, (5, 5), 1)
    img_threshold = cv2.adaptiveThreshold(img_blurr, 255, 1, 1, 11, 2)
    return img_threshold


def find_contours(img, img_threshold):
    img_contours = img.copy()
    contours, hirerarchy = cv2.findContours(
        img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 3)
    return img_contours, contours, hirerarchy


def find_biggest_contour(contours):
    biggest = np.array([])
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:  # avoiding small contours which are essentially noise
            perimiter = cv2.arcLength(contour, True)
            shape_approx = cv2.approxPolyDP(contour, 0.02*perimiter, True)
            if len(shape_approx) == 4 and area > max_area:
                max_area = area
                biggest = shape_approx
    return biggest, max_area


def draw_biggest_contour(img, contours):
    biggest_contour, _ = find_biggest_contour(contours)
    img_biggest_contour = img.copy()
    cv2.drawContours(img_biggest_contour, biggest_contour, -1, (0, 0, 255), 25)
    return img_biggest_contour


def extract_soduko(img, contours):
    # biggest_contour,_ = find_biggest_contour(contours)
    pass


def reorder_biggest_contour(biggest_contour):
    max_width = 0
    max_width_ind = -1
    max_height = 0
    max_height_ind = -1
    for vertex in biggest_contour:
        # if vertex
        pass
    pass


if __name__ == "__main__":
    main()
