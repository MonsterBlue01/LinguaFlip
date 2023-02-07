import numpy as np
import cv2

train_data = np.concatenate([np.fromfile("data_batch_1.bin", dtype=np.uint8),
                            np.fromfile("data_batch_2.bin", dtype=np.uint8),
                            np.fromfile("data_batch_3.bin", dtype=np.uint8),
                            np.fromfile("data_batch_4.bin", dtype=np.uint8),
                            np.fromfile("data_batch_5.bin", dtype=np.uint8)])

test_data = np.fromfile("test_batch.bin", dtype=np.uint8)

train_data = train_data.reshape(-1, 32, 32, 3)
test_data = test_data.reshape(-1, 32, 32, 3)

np.random.shuffle(train_data)
val_data = train_data[:5000]
train_data = train_data[5000:]

train_data = np.array([cv2.resize(image, (224,224)) for image in train_data])
val_data = np.array([cv2.resize(image, (224,224)) for image in val_data])
test_data = np.array([cv2.resize(image, (224,224)) for image in test_data])