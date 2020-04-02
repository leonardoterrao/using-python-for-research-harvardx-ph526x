#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:16:06 2020

@author: leonardo
"""

# WEEK 1 - EX 2

"""

Exercise 2
Consider a circle inscribed in a square. The ratio of their areas (the ratio of the area of the circle to the area of the square) is   π/4  . In this six-part exercise, we will find a way to approximate this value.

"""

"""
Exercise 2a

Using the math library, calculate and print the value of π4.

What is the value of π/4?
Report your answer to 6 decimal places.

"""

import math

math.pi / 4


"""
Exercise 2b

Using random.uniform(), create a function rand() that generates a single float between −1 and 1.

Call rand() once. For us to be able to check your solution, we will use random.seed() to fix the seed value of the random number generator.

We include some sample code to get you started:
    
    import random
    
    random.seed(1) # Fixes the seed of the random number generator.
    
    def rand():
       # define `rand` here!
    
    rand()

What is the value you get from calling rand()? R: -0.7312715117751976
"""

import random

random.seed(1) # Fixes the seed of the random number generator.

def rand():
    return random.uniform(-1,1)

print(rand())


"""
Exercise 2c

The distance between two points x and y is the square root of the sum of squared differences along 
each dimension of x and y. Write a function distance(x, y) that takes two vectors as its input and 
outputs the distance between them. Use your function to find the distance between  x=(0,0)  and  y=(1,1) .

What is the distance between x and y?
"""

import math

def distance(x, y):
    first_var = (y[0]-x[0])**2
    second_var = (y[1]-x[1])**2
    distance = math.sqrt(first_var + second_var)
    return distance
    
x=(0,0)
y=(1,1)
print(distance(x,y))


"""
Exercise 2d

Write a function in_circle(x, origin) that determines whether a point in a two dimensional plane falls within a unit circle surrounding a given origin.

Your function should return a boolean True if the distance between x and origin is less than 1 and False otherwise.

Use distance(x, y) as defined in Exercise 2c.

Use your function to determine whether the point (1,1) lies within the unit circle centered at (0,0):

    def in_circle(x, origin = [0,0]):
       # Define your function here!
       
Does the point (1,1) lie within the unit circle centered at (0,0)? False

"""

import random
import math

random.seed(1)
def in_circle(x, origin = [0]*2):
    if distance(x, origin) < 1:
        return True
    else:
        return False

x = (1, 1)
print(in_circle(x, origin = [0]*2))


"""
Exercise 2e

Create a list inside of R=10000 booleans that determines whether or not a point falls within the unit circle centered at (0,0).

Set the seed to 1 using random.seed(1).

Use the rand function from Exercise 2b to generate R randomly located points.

Use the function in_circle to test whether or not a given pint falls within the unit circle.

Find the proportion of points that fall within the circle by summing all True values in the inside list; then divide the answer by R to obtain a proportion.

Print your answer. This proportion is an estimate of the ratio of the two areas!

What is the proportion of points within the unit circle?
"""

R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(x[i], origin = [0]*2))

print(sum(inside)/R)


"""
Exercise 2f

Calculate the difference between your estimate from Exercise 2e and math.pi / 4. Note: inside and R are defined as in Exercise 2e.

What is the difference between our estimate from 2e and the true value of π / 4 ?
"""

print(math.pi / 4 - sum(inside) / R)

