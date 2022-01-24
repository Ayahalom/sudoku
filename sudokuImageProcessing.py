import cv2
import numpy as np


def pre_processing(img_path, size=None):
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
    img, img_blank = pre_processing(img_path)
    cv2.imshow("Trying", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
