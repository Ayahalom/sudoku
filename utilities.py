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


def reorder_biggest_contour(biggest_contour):
    current_points = biggest_contour.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), dtype=np.int32)
    add = current_points.sum(1)
    new_points[0] = current_points[np.argmin(add)]
    new_points[3] = current_points[np.argmax(add)]
    diff = np.diff(current_points, axis=1)
    new_points[1] = current_points[np.argmin(diff)]
    new_points[2] = current_points[np.argmax(diff)]
    return new_points


def extract_soduko(img, contours, target_width=450, target_height=450):
    biggest_contour, _ = find_biggest_contour(contours)
    biggest_contour = reorder_biggest_contour(biggest_contour)
    source_perspective = np.float32(biggest_contour)
    target_perspective = np.float32([[0, 0], [target_width, 0], [
                                    0, target_height], [target_width, target_height]])
    transform_matrix = cv2.getPerspectiveTransform(
        source_perspective, target_perspective)
    img_soduko = cv2.warpPerspective(
        img, transform_matrix, (target_width, target_height))
    return img_soduko


def split_soduko(img_sudoku):
    boxes = []
    rows = np.vsplit(img_soduko, 9)
    for row in rows:
        cols = no.hsplit(row, 9)
        for col in cols:
            boxes.append(col)
    return boxes


if __name__ == "__main__":
    main()
