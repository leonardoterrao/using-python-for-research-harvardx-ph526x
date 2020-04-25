#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:37:26 2020

@author: leonardo
"""

#3.2.1 Introduction to Language Processing
text =  "This is my test text. We're keeping this text short to keep things manageable."

def count_words(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts.
    """
    text = text.lower()
    skips = [".", ",", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = {}
    for word in (text.split(" ")):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

count_words(text)

################################################################################

from collections import Counter

def count_words_fast(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts.
    """
    text = text.lower()
    skips = [".", ",", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    return word_counts

count_words_fast(text)


count_words_fast(text) == count_words(text)


#3.2.1 Comprehension Check
#len(count_words("This comprehension check is to check for comprehension."))
#count_words(text) is count_words_fast(text)


#3.2.2 Counting Words
def read_book(title_path):
    """
    Read a book and return it as a string
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text;


text = read_book("./books/English/shakespeare/Romeo and Juliet.txt")

len(text)
ind = text.find("What's in a name?")


sample_text = text[ind : ind + 1000]
sample_text


#3.2.3 Reading in a Book
def word_stats(word_counts):
    """Return number of unique words and word frequencies"""
    number_unique = len(word_counts)
    counts = word_counts.values()
    return (number_unique, counts)

text = read_book("./books/English/shakespeare/Romeo and Juliet.txt")
word_counts = count_words(text)
(number_unique, counts) = word_stats(word_counts)
print(number_unique, sum(counts))

text = read_book("./books/German/shakespeare/Romeo und Julia.txt")
word_counts = count_words(text)
(number_unique, counts) = word_stats(word_counts)
print(number_unique, sum(counts))

text = read_book("./books/Portuguese/shakespeare/Romeo e Julieta.txt")
word_counts = count_words(text)
(number_unique, counts) = word_stats(word_counts)
print(number_unique, sum(counts))


#3.4.5 Reading Multiple Files
import os
import pandas as pd

book_dir = "./books"
stats = pd.DataFrame(columns= ("language", "author", "title", "length", "unique"))



title_num = 1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (number_unique, counts) = word_stats(count_words_fast(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), number_unique
            title_num += 1

stats.head()
stats.tail()


#import pandas as pd
#
#table = pd.DataFrame(columns = ("name", "age"))
#table.loc[1] = "Leonardo", 28
#table.loc[2] = "Marcela", 26
#
#table.columns


#3.4.6 Plotting Book Statistics
import matplotlib.pyplot as plt

plt.plot(stats.length, stats.unique, "bo")
plt.loglog(stats.length, stats.unique, "bo")


plt.figure(figsize= (10, 10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique word")
plt.savefig("lang_plot.pdf")


