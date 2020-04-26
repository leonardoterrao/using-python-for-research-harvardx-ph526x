#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:28:44 2020

@author: leonardo
"""

import os
import pandas as pd
import numpy as np
from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)
    
    
    
    
# ex 1
hamlets = pd.read_csv('hamlets.csv', usecols=range(1,3))
print(hamlets)


# ex 2
language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)
data = pd.DataFrame( {'word': list(counted_text.keys()), 'count': list(counted_text.values()) })
data.loc[data['word'] == 'hamlet']


#ex 3
data['lenght'] = data['word'].apply(len)
data['frequency'] = np.where(data['count'] > 10, 'frequent', np.where(data['count'] == 1, 'unique', 'infrequent'))

len(data.loc[data['frequency'] == 'unique'])


#ex 4
sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(['frequency']).mean()['lenght'],
        "num_words": data.groupby(by = "frequency").size()
})
    
sub_data.loc[sub_data["frequency"] == "infrequent"]
    
    



def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)
    

#ex 5
grouped_data = pd.DataFrame(columns = ["language", "frequency", "mean_word_length", "num_words"])

for i in range(hamlets.shape[0]):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)





print(grouped_data[(grouped_data.language == "German") & (grouped_data.frequency == "frequent")]["mean_word_length"])
print(grouped_data[(grouped_data.language == "Portuguese") & (grouped_data.frequency == "frequent")]["num_words"])
grouped_data


#ex 6
colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
# write your code to display the plot here!

plt.show()












