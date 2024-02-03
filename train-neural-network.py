import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Assuming you have training_data and labels
# Replace them with your actual data
# Ensure that your labels are one-hot encoded for categorical crossentropy

# Generate some dummy data for demonstration
import numpy as np

input_size = 4
# Replace 1000 with your actual number of samples
train_data = np.random.random((1000, input_size))
labels = np.random.randint(2, size=(1000, 1))  # Assuming binary classification

# Define the model
model = keras.Sequential([
    layers.Input(shape=(input_size,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='softmax')
])

print(train_data)
print(labels)

# Compile the model
# model.compile(optimizer='adam', loss='categorical_crossentropy',
#               metrics=['accuracy'])
#
# # Train the model
# model.fit(train_data, labels, epochs=10, batch_size=32, validation_split=0.2)
# # Adjust the number of epochs, batch size, and validation split based on your requirements
#
# # Save the trained model
# model.save('your_model.h5')
