#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:37:47 2020

@author: leonardo
"""

#4.1.2
import numpy as np
import pandas as pd

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")


#First five lines
whisky.head()
#Last five lines
whisky.tail()


#show rows 5 to 10 and columns 0 to 5
whisky.iloc[5:10, 0:5]

flavors = whisky.iloc[:, 2:14]

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

#4.1.3
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors, cmap = "jet")
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())

plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky, cmap = "jet")
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")


#4.1.4
from sklearn.cluster.bicluster import SpectralCoclustering
model = SpectralCoclustering(n_clusters = 6, random_state = 0)
model.fit(corr_whisky)
model.rows_

np.sum(model.rows_, axis=1)

model.row_labels_

#4.1.5
whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop = True)

correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlations = np.array(correlations)

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky, cmap = "jet")
plt.title("Original")
plt.axis("tight")
plt.subplot("122")
plt.pcolor(correlations, cmap = "jet")
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")





#4.1.5 ex 1
import pandas as pd
data = pd.Series([1,2,3,4])
data = data.ix[[3,0,1,2]]
data[0]



#4.1.5 ex 2
import pandas as pd
data = pd.Series([1,2,3,4])
data = data.ix[[3,0,1,2]]
data = data.reset_index(drop=True)
data[0]
