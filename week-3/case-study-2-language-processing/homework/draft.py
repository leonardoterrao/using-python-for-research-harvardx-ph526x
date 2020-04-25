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
    
    