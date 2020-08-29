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
# from sklearn.linear_model import SGDClassifier
# from sklearn.neural_network import MLPClassifier

# from keras.models import Sequential
# from keras.layers import Dense, Dropout, BatchNormalization
# from keras.wrappers.scikit_learn import KerasClassifier

# def build_model():
#     model = Sequential()
#     model.add(Dense(64, activation='relu', input_dim=20, kernel_initializer='uniform'))
#     model.add(Dropout(0.5))
#     model.add(Dense(32, activation='relu', kernel_initializer='uniform'))
#     model.add(Dropout(0.5))
#     model.add(Dense(1, activation='sigmoid', kernel_initializer='uniform'))
#     model.compile(optimizer = 'rmsprop', 
#               loss='binary_crossentropy', metrics=['accuracy'])
#     return model

from sklearn.ensemble import GradientBoostingClassifier

clf =  GradientBoostingClassifier(n_estimators=20, learning_rate=0.1, max_features=2, max_depth=2, random_state=0)
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

acc = clf.score(X_test, y_test)
print('Accuracy : ',acc)

from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred) 
print(report)

with open("metrics.txt", 'w') as outfile:
        outfile.write("Accuracy: " + str(acc) + "\n")


f=open("metrics.txt", "a+")
f.write("```")
f.write(report)
f.write("```")

f.close()
# Plot it
disp = plot_confusion_matrix(clf, X_test, y_test, normalize='true',cmap=plt.cm.Blues)
plt.savefig('confusion_matrix.png')

