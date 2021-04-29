import fasttext
import re

def strip_formatting(string):
    string = string.lower()
    string = re.sub(r"([.!?,'/()])", r" \1 ", string)
    return string

# Reviews to check
reviews = [
    "This restaurant literally changed my taste. This is the best food I've ever eaten!",
    "The place is good I think. I heard from my friend.",
    "I am very much disappointed with the service. I will never use this service again."
]

# Pre-process the text of each review so it matches the training format
preprocessed_reviews = list(map(strip_formatting, reviews))

# Load the model
classifier = fasttext.load_model('review_rating_model.bin')

# Get fasttext to classify each review with the model
labels, probabilities = classifier.predict(preprocessed_reviews, 1)

# Print the results
for review, label, probability in zip(reviews, labels, probabilities):
    stars = int(label[0][-3])
    print("{} ({}% confidence)".format("☆" * stars, int(probability[0] * 100)))
    print(review)