from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import json
import os
import numpy as np
# Read in data
X_train = np.genfromtxt("data/train_features.csv")
y_train = np.genfromtxt("data/train_labels.csv")
X_test = np.genfromtxt("data/test_features.csv")
y_test = np.genfromtxt("data/test_labels.csv")


# Fit a model


# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB 
# from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier

clf = SGDClassifier(eta0=1, max_iter=1000, tol=0.0001, alpha=0.01, l1_ratio=1.0, learning_rate='adaptive', loss='log', penalty='elasticnet')

clf.fit(X_train,y_train)

acc = clf.score(X_test, y_test)
print(acc)
with open("metrics.txt", 'w') as outfile:
        outfile.write("Accuracy: " + str(acc) + "\n")


# Plot it
disp = plot_confusion_matrix(clf, X_test, y_test, normalize='true',cmap=plt.cm.Blues)
plt.savefig('confusion_matrix.png')

