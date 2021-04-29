import fasttext


def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))

# Train the model
model = fasttext.train_supervised('fasttext_dataset_training.txt')
model.save_model("review_rating_predict.bin")

# Load the model and show accuracy
model = fasttext.load_model("review_rating_predict.bin")
print_results(*model.test('fasttext_dataset_test.txt'))
