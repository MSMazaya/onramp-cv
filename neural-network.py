from tensorflow import keras
from tensorflow.keras import layers

input_size = 200 * 200

model = keras.Sequential([
    layers.Input(shape=(input_size,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()
