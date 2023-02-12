import tensorflow as tf
import numpy as np
from model import build_model
from data_preprocessing import train_data, val_data

X_train = train_data / 255.0
X_val = val_data / 255.0

model = build_model()

history = model.fit(X_train, Y_train, epochs=10, batch_size=32, validation_data=(X_val, Y_val))

model.save('model.h5')