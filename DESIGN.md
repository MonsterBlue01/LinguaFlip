# DESIGN

## Files:

- `data_preprocessing.py`
    - This is where the whole project starts. [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) images as a data set (the copyright statement for the CIFAR-10 creator is in the `COPYRIGHT` file) seems to be a good choice. Since there are only training and test data sets in the data set, in data_preprocessing.py, the test data set needs to be retained, the training data set is disrupted and the first five thousand are assigned as the verification data set. In the end, you need to use OpenCV to convert the format of all pictures to (224, 224) format.
- `model.py`
    - The code in `model.py` defines a Convolutional Neural Network (CNN) using the TensorFlow library with the Keras API. The network consists of two Convolutional Layers and two Max Pooling Layers, followed by three Dense Layers. The input to the network is an image of shape (224,224,3), where the last dimension refers to the red, green and blue color channels of the image. The first Convolutional Layer has 6 filters of size (5,5), followed by a Max Pooling Layer of size (2,2). The second Convolutional Layer has 16 filters of size (5,5) and is followed by another Max Pooling Layer of size (2,2). The output of the Max Pooling Layers is then flattened and passed through two Dense Layers with 120 and 84 neurons respectively. The final Dense Layer has 10 neurons and uses a softmax activation function to output a probability distribution over the 10 classes in the CIFAR-10 dataset. The model is compiled using the Adam optimization algorithm with categorical crossentropy as the loss function and accuracy as the evaluation metric.
- `evaluate.py`
- `predict.py`
- `train.py`
- `utils.py`