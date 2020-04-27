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