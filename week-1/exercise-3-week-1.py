#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:53:23 2020

@author: leonardo
"""

# WEEK 1 - EX 3

"""

Exercise 3
A list of numbers representing measurements obtained from a system of interest can often be noisy. One way to deal with noise to smooth the values by replacing each value with the average of the value and the values of its neighbors. We will practice data smoothing in this three-part exercise.
"""

"""
Exercise 3a

Write a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors n_neighbors on either side of a given member of the list to consider.

For each value in x, moving_window_average(x, n_neighbors) computes the average of the value and the values of its neighbors.

moving_window_average
If there are not enough neighbors (for cases near the edge), substitute the original value for a neighbor for each missing neighbor.

Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors=1.

Here is some code to get you started:

    def moving_window_average(x, n_neighbors=1):
        n = len(x)
        width = n_neighbors*2 + 1
        x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
        # To complete the function,
        # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    
    x = [0,10,5,3,1,5]
    print(moving_window_average(x, 1))
    
What is the sum of the moving window averages? R: 24.000000000000004
"""

import random

random.seed(1) #Initialize the basic random number generator.

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    meanValues = []
    for i in range(1, n+1):
        meanValues.append((x[i-1] + x[i] + x[i+1])/width)
    return meanValues

x = [0,10,5,3,1,5]
print(sum(moving_window_average(x, 1)))


"""
Exercise 3b

Compute and store R=1000 random values from 0-1 as x.

Compute the moving window average for x for values of n_neighbors ranging from 1 to 9 inclusive.

Store x as well as each of these averages as consecutive lists in a list called Y.

Use this code to get started:

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
# write your code here!
What is the moving window average for the 10th entry in x for n_neighbors = 5? R: 0.45325045824763405
"""

import random

random.seed(1) #Initialize the basic random number generator.


R = 1000
x = []
Y= []
for i in range(R):
    num = random.uniform(0,1)
    x.append(num)
Y.append(x)

for i in range(1,10):
    mov_avg = moving_window_average(x, n_neighbors=i)
    Y.append(mov_avg) 


sum(x[4:15])/11


"""
Exercise 3c

For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.

Print your answer. As the window width increases, does the range of each list increase or decrease? Why do you think that is?

As window width increases, does the range of each list increase or decrease? R: Decrease
"""

ranges = [max(i) - min(i) for i in Y]
print(ranges)

