# Playing with Data
This repository features a collection of Jupyter notebooks exploring data science concepts.


  * [best_practices.ipynb](./best_practices.ipynb) ([nbviewer](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/best_practices.ipynb)) demonstrate best practices and model evaluation metrics.  Notebook topics include:

      * [pipelining](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/best_practices.ipynb#Pipeline)
      * [learning curves](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/best_practices.ipynb#Learning-Curves)
      * [validation curves](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/best_practices.ipynb#Validation-Curves)
      * [confusion matrix](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/best_practices.ipynb#Confusion-Matrix)
      * [receiver operator characteristics (ROC and AUC) ](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/best_practices.ipynb#Receiver-Operator-Characteristic)
  * [digits with bokeh.ipynb](./digits%20with%20bokeh.ipynb) ([nbviewer](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/digits%20with%20bokeh.ipynb)) demonstrates using [Bokeh](http://bokeh.pydata.org/en/latest) to visualize the mNIST digits data.
  * [sci-data_with_datashader.ipynb](./sci-data_with_datashader.ipynb) ([nbviewer](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/sci-data_with_datashader.ipynb)) demonstrates using [Datashader](http://datashader.readthedocs.io/en/latest/) to accurately plot tens-of-thousands to millions of data points.
  * [mnist_shallow_learning.ipynb](./mnist_shallow_learning.ipynb) ([nbviewer](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/mnist_shallow_learning.ipynb])) is [the beginnings of] a machine learning model (not using deep learning) to classify handwritten digits using either [supervised](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/mnist_shallow_learning.ipynb#Start-with-the-K-nearest-Neighbor-Classifier-(using-default-5-neighbors)) or [unsupervised](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/mnist_shallow_learning.ipynb#What-if-we-treat-this-as-unsupervised-learning,-i.e,-cluster-the-digits-without-considering-the-labels?) learning.
  * [mnist_shallow_learning.ipynb](mnist_shallow_learning.ipynb) ([nbviewer](http://nbviewer.jupyter.org/github/StevenCHowell/playing_with_data/blob/master/mnist_shallow_learning.ipynb)) is [the beginnings of] a reproduction of [Mason Victor's](http://www.recursionpharma.com/mason.html) [SciPy 2016 lightning talk](https://www.youtube.com/watch?v=sv9S-25XKe4&feature=youtu.be&t=54m40s) demonstrating a deep  learning model (using [theano](http://deeplearning.net/software/theano/) together with [keras](https://keras.io/)) to classify handwritten digits.

Subdirectories within this repo contain the following:
  * [hands_on_machine_learning/](https://github.com/StevenCHowell/playing_with_data/tree/master/hands_on_machine_learning) contains [the beginnings of] a collection of notebooks reproducing/exploring the concepts presentid in Aurélien Géron's book [Hands-On Machine Learning with Scikit-Learn and TensorFlow](http://shop.oreilly.com/product/0636920052289.do).
  * [bayes_problems/](https://github.com/StevenCHowell/playing_with_data/tree/master/bayes_problems) contains a series of sample Bayes' theorem problems and solutions.
  * [playlist_predictor/](https://github.com/StevenCHowell/playing_with_data/tree/master/playlist_predictor) contains [the skeleton of] a project to use supervised machine learning to build a playlist of songs based on the consistentency of seed songs.
