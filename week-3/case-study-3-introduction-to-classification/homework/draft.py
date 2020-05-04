#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:09:00 2020

@author: leonardo
"""

# DO NOT EDIT
import numpy as np, random, scipy.stats as ss

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]


#ex 1
import pandas as pd

wines = pd.read_csv('wine.csv')
wines.head()


#ex 2
wines = wines.rename(columns={"color": "is_red"})
wines['is_red'] = wines['is_red'].replace('red', 1)
wines['is_red'] = wines['is_red'].replace('white', 0)
numeric_data = wines.copy()
numeric_data
sum(numeric_data['is_red'])

numeric_data.shape



#ex 3
import sklearn.preprocessing
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(data=scaled_data, columns=numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)

principal_components.shape






#ex 4
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]
plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2, c = numeric_data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()





#ex 5
import numpy as np 
np.random.seed(1) # do not change

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)


np.sum(x == y)

def accuracy(predictions, outcomes):
    same_values = np.sum(predictions == outcomes);
    return 100 * same_values / len(outcomes)


print(accuracy(x, y))


#ex 6
print(accuracy(0, wines['high_quality']))


#ex 7
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, wines['high_quality'])
# Enter your code here!
library_predictions = knn.predict(numeric_data)
accuracy = accuracy(library_predictions, wines['high_quality'])
print(accuracy)


#ex 8
import random
n_rows = wines.shape[0] # same as len(data)
random.seed(123)
selection = random.sample(range(n_rows), 10)


#ex 9
predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(wines["high_quality"])

my_predictions = [knn_predict(p, predictors[training_indices,:], outcomes, k=5) for p in predictors[selection]]
percentage = accuracy(my_predictions, wines.high_quality[selection])

print(percentage)















