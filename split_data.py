import json
from pathlib import Path
import re
import random

# Dataset path
reviews_data = Path("../../Datasets/yelp/yelp_academic_dataset_review.json")

# Training and Test data path
training_data = Path("fasttext_dataset_training.txt")
test_data = Path("fasttext_dataset_test.txt")

# Test data amount
percent_test_data = 0.10


def strip_formatting(string):
    string = string.lower()
    string = re.sub(r"([.!?,'/()])", r" \1 ", string)
    return string


with open(reviews_data, 'r', encoding='utf-8') as input, open(training_data, 'w', encoding='utf-8') as train_output, open(test_data, 'w', encoding='utf-8') as test_output:
    for line in input:
        review_data = json.loads(line)

        rating = review_data['stars']
        text = review_data['text'].replace("\n", " ")
        text = strip_formatting(text)

        fasttext_line = "__label__{} {}".format(rating, text)

        if random.random() <= percent_test_data:
            test_output.write(fasttext_line + "\n")
        else:
            train_output.write(fasttext_line + "\n")