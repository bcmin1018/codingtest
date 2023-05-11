import numpy as np

class NaiveBayesClassifier:
    def __init__(self):
        self.vocab = set()
        self.class_probs = {}
        self.word_probs = {}
        self.word_counts = {}

    def fit(self, X, y):
        # Create vocabulary set
        for doc in X:
            self.vocab.update(doc)

        # Calculate class probabilities
        total_docs = len(y)
        for c in np.unique(y):
            num_docs_in_class = np.sum(y == c)
            # print('num_docs_in_class ', num_docs_in_class)
            self.class_probs[c] = num_docs_in_class / total_docs

        # Calculate word probabilities
        self.word_counts = {word: 0 for word in self.vocab}
        total_words = 0
        for c in np.unique(y):
            docs_in_class = [x for x, y in zip(X, y) if y == c]
            for doc in docs_in_class:
                for word in doc:
                    self.word_counts[word] += 1
                    total_words += 1
                self.word_probs[c] = {word: count / total_words for word, count in self.word_counts.items()}
        # for c in np.unique(y):
        #     # docs_in_class = X[y == c]
        #     docs_in_class = X[y == int(c)]
        #     # print('docs_in_class ', docs_in_class)
        #     self.word_counts = {word: 0 for word in self.vocab}
        #     total_words = 0
        #     # print('word_counts ', word_counts)
        #     print('docs_in_class ', docs_in_class)
        #     for doc in docs_in_class:
        #         # self.word_counts[word] +=1
        #         # total_words += 1
        #         for word in doc:
        #             self.word_counts[word] += 1
        #             total_words += 1
        #     self.word_probs[c] = {word: count / total_words for word, count in self.word_counts.items()}
        # print('word_counts: ', word_counts)
        # print('total_words: ', total_words)

    def predict(self, X):
        y_pred = []
        for doc in X:
            ham_prob = np.log(self.class_probs[0])
            spam_prob = np.log(self.class_probs[1])
            for word in doc:
                if word in self.vocab:
                    ham_prob += np.log(self.word_probs[0][word])
                    spam_prob += np.log(self.word_probs[1][word])
            if ham_prob > spam_prob:
                y_pred.append(0)
            else:
                y_pred.append(1)
        return y_pred

from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from collections import Counter

# Load the dataset
data = fetch_20newsgroups(subset='all', categories=['alt.atheism', 'talk.religion.misc'])
X, y = data.data, data.target

# Preprocess the data
X = [doc.lower().split() for doc in X]
y = [0 if label == 0 else 1 for label in y]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the classifier
nb = NaiveBayesClassifier()
nb.fit(X_train, y_train)