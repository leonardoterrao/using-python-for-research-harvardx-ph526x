#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:14:16 2020

@author: leonardo
"""


# WEEK 1 - EX 1

"""

Exercise 1
In this five-part exercise, we will count the frequency of each letter in a given string.

""""

""""
Exercise 1a
Import the string library.

Create a variable alphabet that consists of the lowercase and uppercase letters in the English alphabet using the ascii_letters data attribute of the string library.

What line of code did you use to create the alphabet variable?
"""

alphabet = string.ascii_letters



"""
#Exercise 1b
The lower and upper case letters of the English alphabet should stored as the string variable alphabet.

Consider the sentence 'Jim quickly realized that the beautiful gowns are expensive'. Create a dictionary count_letters with keys consisting of each unique letter in the sentence and values consisting of the number of times each letter is used in this sentence. Count upper case and lower case letters separately in the dictionary.

What is the 3rd value of the dictionary? R: 1 
What is the 8th value of the dictionary? R: 3
"""

def count_letters(phrase):
    dictonary = {}
    for i in range(0, len(phrase)):
        if (phrase[i] not in alphabet):
            continue
        
        if (phrase[i] in dictonary):
            dictonary[phrase[i]] = dictonary[phrase[i]] + 1
        else:
            dictonary[phrase[i]] = 1
    return(dictonary)


count_letters('Jim quickly realized that the beautiful gowns are expensive')


"""
Exercise 1c

Rewrite your code from Exercise 1b to make a function called counter that takes a string input_string and returns a dictionary of letter counts count_letters.

Use your function to call counter(sentence).

What is the correct function header for the counter function?
"""

#def counter(input_string, letter):


"""
Exercise 1d

Abraham Lincoln was a president during the American Civil War. His famous 1863 Gettysburg Address has been stored as address. Use the counter function from 1c to return a dictionary consisting of the count of each letter in this address and save it as address_count.


"""
address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""

"""
How many times does the letter h appear in the Gettysburg Address?
"""

def counter(input_string, letter):
    dictonary = {}
    for i in range(0, len(input_string)):
        if (input_string[i] not in alphabet):
            continue
        
        if (input_string[i] in dictonary):
            dictonary[input_string[i]] = dictonary[input_string[i]] + 1
        else:
            dictonary[input_string[i]] = 1

    return(dictonary[letter])


counter(address, 'h')

"""
Exercise 1e

In Exercise 1d, you stored the frequency of each letter in the Gettysburg Address is in address_count. Use this dictionary to find the most common letter in the Gettysburg address.

What is the most frequent letter in the Gettysburg Address?
"""

def most_common_letter(input_string):
    dictonary = {}
    for i in range(0, len(input_string)):
        if (input_string[i] not in alphabet):
            continue
        
        if (input_string[i] in dictonary):
            dictonary[input_string[i]] = dictonary[input_string[i]] + 1
        else:
            dictonary[input_string[i]] = 1

    return(max(dictonary, key=dictonary.get))


most_common_letter(address)
