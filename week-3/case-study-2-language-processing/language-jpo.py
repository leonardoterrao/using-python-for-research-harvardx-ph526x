#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:37:26 2020

@author: leonardo
"""

#3.2.1
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


#Comprehension Check 3.2.2
#len(count_words("This comprehension check is to check for comprehension."))
#count_words(text) is count_words_fast(text)


#3.2.3
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


#3.2.4
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

















