import tensorflow as tf
from tenserflow import keras

def build_model():
    model = keras.Sequential([
        keras.layers.Conv2D(6, (5,5), activation='relu', input_shape=(224,224,3)),
        keras.layers.MaxPooling2D(2,2),
        keras.layers.Conv2D(16, (5,5), activation='relu'),
        keras.layers.MaxPooling2D(2,2),
        keras.layers.Flatten(),
        keras.layers.Dense(120, activation='relu'),
        keras.layers.Dense(84, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model