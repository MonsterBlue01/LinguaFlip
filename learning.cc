// Convolutional Neural Network (CNN): The model defined in the code is a type of deep learning neural network specifically designed for image classification tasks.

// Layers: In this code, the model is constructed using several types of layers, including Conv2D, MaxPooling2D, Flatten, and Dense. Each layer serves a specific purpose in the network and helps extract meaningful features from the input image.

// Activation Functions: Each layer in the network is associated with an activation function, which is used to introduce non-linearity into the network. In this code, the ReLU activation function is used.

// Input Shape: The input shape argument in the first Conv2D layer specifies the dimensions of the input images that the network will receive.

// Pooling Layers: The MaxPooling2D layers serve to down-sample the input, effectively reducing the spatial dimensionality of the input and helping to combat overfitting.

// Flattening: The Flatten layer takes the output from the previous layer, which has a multi-dimensional shape, and converts it into a one-dimensional array.

// Dense Layers: The Dense layers are fully connected layers, which means that each neuron in a dense layer is connected to every neuron in the previous layer.

// Output Layer: The final Dense layer in this code produces the final prediction for the image, using the softmax activation function, which outputs the class probabilities.

// Compilation: The model is then compiled using the 'adam' optimizer, the categorical crossentropy loss function, and accuracy as the evaluation metric.