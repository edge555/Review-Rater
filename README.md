# Review Rater

Review rating model to rate reviews with stars and confidence using FastText.

# Requirements

* [FastText](https://github.com/facebookresearch/fastText/tree/master/python#building-fasttext)

# Dataset

* [yelp_academic_dataset_review.json](https://www.kaggle.com/yelp-dataset/yelp-dataset?select=yelp_academic_dataset_review.json) 

# How to run

* Install FastText in the directory.

* Download the json file.

* Run split_data.py to produce training and testing datasets.

* Run train_model.py to train and save the model.

* Run main.py to run the model. Change the 'reviews' array to test different reviews.
