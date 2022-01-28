import cv2
import numpy as np
import utilities


def load_img(img_path, size=None):
    img = cv2.imread(img_path)
    if size is not None:
        img = cv2.resize(img, (size, size))
        img_blank = np.resize((size, size, 3), np.uint8)
    else:
        img_blank = np.zeros((img.shape[0], img.shape[0], 3), np.uint8)
    return img, img_blank


def finding_sudoku():
    pass


def extracting_sudoku():
    pass


def main():
    img_path = "C:\shurim\CS\Projects\Sudoku\material\solvable_sudoku_with_hidden_singles.png"
    img, img_blank = load_img(img_path)
    img_threshold = utilities.preprocess_img(img)
    img_contours, contours, hirerarchy = utilities.find_contours(
        img, img_threshold)
    biggest_contour, max_area = utilities.find_biggest_contour(contours)
    img_biggest_contour = utilities.draw_biggest_contour(img, contours)
    img_sudoku = utilities.extract_soduko(img, contours)
    boxes = utilities.split_soduko(img_sudoku)
    cv2.imshow("image", boxes[2])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
