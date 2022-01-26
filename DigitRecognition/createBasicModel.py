import pickle
import numpy as np
import tensorflow as tf
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('INFO')


def load_mnist():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    return (x_train, y_train), (x_test, y_test)


def create_model(num_layers, neurons_per_layer, mnist_shape):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(mnist_shape, mnist_shape)))
    for i in range(0, num_layers):
        model.add(tf.keras.layers.Dense(
            units=neurons_per_layer, activation='relu'))
    model.add(tf.keras.layers.Dense(
        units=neurons_per_layer, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


def train_model(x_train=None, y_train=None, num_layers=2, neurons_per_layer=128, mnist_shape=28, Epochs=5):
    #     if x_train is None or y_train is None:
    #     (x_train, y_train), (x_test, y_test) = load_mnist()
    # if model is None:
    #     model = create_model(num_layers, neurons_per_layer, mnist_shape)
    (x_train, y_train), (x_test, y_test) = load_mnist()
    model = create_model(num_layers, neurons_per_layer, mnist_shape)
    model.fit(x_train, y_train, epochs=Epochs)
    return model, (x_train, y_train), (x_test, y_test)


def model_loss_and_accuracy(model, x_test, y_test):
    loss, accuracy = model.evaluate(x_test, y_test)
    return loss, accuracy


def test_with_image(model, img):
    img = cv2.imread(img)[:, :, 0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    print(np.argmax(prediction))


def save_model(model, file):
    with open(file, 'wb') as f:
        pickle.dump(model, f)
    print(f'model saved succsessfully to {file}')
    # model.save('digits.model')


def load_model(file):
    with open(file, 'rb') as f:
        model = pickle.load(f)
    return model


# def silance_tf_warnings():
#     os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def main():
    model, (x_train, y_train), (x_test, y_test) = train_model(
        Epochs=3, num_layers=3)
    loss, accuracy = model_loss_and_accuracy(model, x_test, y_test)
    print(
        f'loss of the model is {loss}, and accuracy of the model is {accuracy}')

    save_model(model, 'model.pickle')
    # model = load_model(
    #     "digits.model")
    test_with_image(model, "test_two_digit.png")


if __name__ == "__main__":
    main()
