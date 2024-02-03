import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def get_training_data():
    data = []

    # Load images of oranges
    for filename in os.listdir('images/oranges'):
        file_path = os.path.join('images/oranges', filename)
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (200, 200))
        edges = cv2.Canny(image, 100, 200)
        flattened_image = edges.flatten()
        data.append(flattened_image)

    # Load images of non-oranges
    for filename in os.listdir('images/non-oranges'):
        file_path = os.path.join('images/non-oranges', filename)
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (200, 200))
        edges = cv2.Canny(image, 100, 200)
        flattened_image = edges.flatten()
        data.append(flattened_image)

    # kalau orange, itu 1
    # kalau bukan orange, itu 0
    labels = np.array([1] * 10 + [0] * (len(data) - 10))
    return np.array(data), labels


data, labels = get_training_data()

model = keras.Sequential([
    layers.Input(shape=(data.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(data, labels, epochs=100,
                    batch_size=10, validation_split=0.1)


def print_prediction(file):
    image = cv2.imread(file, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (200, 200))
    edges = cv2.Canny(image, 100, 200)
    flattened_image = np.array(edges.flatten())
    input_for_prediction = flattened_image.reshape(1, -1)
    predictions = model.predict(input_for_prediction)
    print("orange" if (predictions[0] > 0.99) else "not orange")


print_prediction("images/oranges/o2.jpeg")
print_prediction("images/oranges/o3.jpeg")
print_prediction("images/oranges/o4.jpeg")
print_prediction("images/non-oranges/no1.jpeg")
print_prediction("images/non-oranges/no2.jpeg")
print_prediction("images/non-oranges/no3.jpeg")
print_prediction("images/non-oranges/no4.jpeg")
print_prediction("images/oranges/o1.jpeg")
