#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import re

__author__ = "msarafriis"


def ver_check():
    if sys.version_info[0] < 3:
        raise Exception('Python 2 is unsupported. Python 3 is required.')


def create_mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it. 
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output: 
            {
                "" : ["I"],
                "I" : ["am", "don't"], 
                "am": ["a"], 
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "I" : ["don't"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    # +++your code here+++
    with open(filename, 'r') as text:
        words = re.sub("[^\w]", " ", text.read()).split()
        found_words = {}
        for word_index in range(0, len(words)):
            word = words[word_index]
            try:
                if (word_index + 1 != len(words)):
                    found_words[word.lower()].append(
                        words[word_index + 1].lower())
            except:
                found_words[word.lower()] = []
                if (word_index + 1 != len(words)):
                    found_words[word.lower()].append(
                        words[word_index + 1].lower())
        return found_words


def print_mimic(mimic_dict, start_word):
    """Given a previously compiled mimic_dict and start_word, prints 200 random words:
        - Print the start_word
        - Lookup the start_word in your mimic_dict and get it's next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    # +++your code here+++
    next_word = ""
    for selection in range(0, 200):
        word = ""
        if selection == 0:
            word = start_word
        else:
            word = next_word
        dictionary = mimic_dict[word]
        print("{}\n".format(word))
        print(", ".join(dictionary))
        next_word = dictionary[random.randrange(len(dictionary))]
        print("\n" * 5)


# Provided main(), calls mimic_dict() and mimic()
def main():
    ver_check()
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    d_words = [key for key in d]
    print_mimic(d, d_words[0])


if __name__ == '__main__':
    main()
