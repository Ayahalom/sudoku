import createBasicModel as bm
import os


def test_images_in_dir(model, directory):
    print(os.listdir(directory))
    for file in os.listdir(directory):
        prediction, success = test_img(model, directory + file)
        print(
            f'the prediction is {prediction} which was a {success} for image {file}')


def test_img(model, file):
    prediction = bm.test_with_image(model, file)
    print(file[-5])
    if prediction == int(file[-5]):
        return prediction, True
    return prediction, False


def main():
    model = bm.load_model("./DigitRecognition/basic_model")
    directory = "C:/shurim/CS/Projects/sudoku/DigitRecognition/ImagesTesting/"
    test_images_in_dir(model, directory)


if __name__ == "__main__":
    main()
