#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:43:57 2020

@author: leonardo
"""

#3.3.1: Introduction to kNN Classification
#3.3.2: Finding the Distance Between Two Points
import numpy as np

def distance(p1, p2):
    """Find the distance between points p1 and p2."""
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

p1 = np.array([1,1])
p2 = np.array([4,4])

distance(p1, p2)


#3.3.3: Majority Vote
import random

def majority_vote(votes):
    """
    Return the most common element in votes.
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
            
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    
    return random.choice(winners)


import scipy.stats as ss

def majority_vote_short(votes):
    """
    Return the most common element in votes.
    """
    mode, count = ss.mstats.mode(votes)
    return mode
            
votes = [1,2,3,1,2,3,1,2,3,3,3,3,2,2,2]
majority_vote(votes)
majority_vote_short(votes)


#3.3.4: Finding Nearest Neighbors

points = np.array([[1, 1], [1, 2], [1, 3], 
                   [2, 1], [2, 2], [2, 3], 
                   [3, 1], [3, 2], [3, 3]])

p = np.array([2.5, 2])

def find_nearest_neighbors(p, points, k=5):
    """Find the k nearest neighbors of point p and return their indices."""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


ind = find_nearest_neighbors(p, points, 2); print(points[ind])
ind = find_nearest_neighbors(p, points, 3); print(points[ind])
ind = find_nearest_neighbors(p, points, 4); print(points[ind])

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])

outcomes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
len(outcomes)

knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2)
knn_predict(np.array([1.0, 2.7]), points, outcomes, k=2)


import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])


#3.3.5: Generating Synthetic Data
def generate_synth_data(n=50):
    """Create two sets of points from bivariate normal distributions"""
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis = 0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)

n = 20
(points, outcomes) = generate_synth_data(n)

plt.figure()
plt.plot(points[:n,0], points[:n,1], "ro")
plt.plot(points[n:,0], points[n:,1], "bo")
plt.savefig("bivariate.pdf")


#3.3.6: Making a Prediction Grid
def make_predicition_grid(predictors, outcomes, limits, h, k):
    """Classify each point on the prediction grid."""
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype = int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k)

    return (xx, yy, prediction_grid)


#3.3.7: Plotting the Prediction Grid
def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)

(predictors, outcomes) = generate_synth_data()

k = 5; filename = "knn_synth_5.pdf"; limits = (-3,4,-3,4); h = 0.1
(xx, yy, prediction_grid) = make_predicition_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

k = 50; filename = "knn_synth_50.pdf"; limits = (-3,4,-3,4); h = 0.1
(xx, yy, prediction_grid) = make_predicition_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)


#3.3.8: Applying the kNN Method

from sklearn import datasets
iris = datasets.load_iris()

predictors = iris.data[:, 0:2]
outcomes = iris.target
plt.plot(predictors[outcomes == 0][:,0], predictors[outcomes == 0][:,1], "ro")
plt.plot(predictors[outcomes == 1][:,0], predictors[outcomes == 1][:,1], "go")
plt.plot(predictors[outcomes == 2][:,0], predictors[outcomes == 2][:,1], "bo")
plt.savefig("iris.pdf")

k = 5; filename = "iris_grid.pdf"; limits = (4,8,1.5,4.5); h = 0.1
(xx, yy, prediction_grid) = make_predicition_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(predictors, outcomes)
sk_predicitons = knn.predict(predictors)

my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])

print(100*np.mean(sk_predicitons == my_predictions))

print(100*np.mean(sk_predicitons == outcomes))
print(100*np.mean(my_predictions == outcomes))






