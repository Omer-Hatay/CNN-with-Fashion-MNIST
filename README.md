<h1>CNN with Fashion MNIST Data Set</h1>
<p>This code involves building and training a Convolutional Neural Network (CNN) model using the Fashion MNIST dataset. 
  First, the dataset is downloaded and the pixel values are normalized to the range [0,1]. Next, the CNN model is defined,
  consisting of two convolutional layers, two max pooling layers, a flatten layer, and two dense (fully connected) layers. 
  The model is compiled using the adam optimizer and sparse_categorical_crossentropy loss function, and then trained on the training data for 5 epochs. Subsequently,
  the model is evaluated on the test data,
  and its accuracy is calculated. Finally,
  a specific test image is predicted by the model, compared to its actual label, and visualized using Matplotlib.</p>

<h2>About Fashion MNIST Data Set</h2>
  <p>The fashion MNIST dataset is a large freely available database of fashion 
images that is commonly used for training and testing various ML systems. The dataset 
contains 70,000 28x28 grayscale images of fashion products from 10 categories from a dataset 
of Zalando article images, with 7,000 images per category. The training set consists of 60,000 
images and the test set consists of 10,000 images. The dataset is commonly included in standard 
machine learning libraries. </p>
<h3>Labels</h3>
<pre>
• 0 T-shirt/top 
• 1 Trouser 
• 2 Pullover 
• 3 Dress 
• 4 Coat 
• 5 Sandal 
• 6 Shirt 
• 7 Sneaker 
• 8 Bag 
• 9 Ankle boot 
</pre>
