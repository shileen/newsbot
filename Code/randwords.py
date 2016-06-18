#!/usr/bin/python
import random

# gets the words from the file and makes a list called "words"


def getcurrentword():
    with open("words.txt", "r") as word_list:
        words = word_list.read().split()
    if not words:
        cur_word = None
    else:
        i = random.randrange(len(words))
        words[i], words[-1] = words[-1], words[i]
        cur_word = words.pop()
        wrdfile = open("words.txt", "w")
        for word in words:
            print>>wrdfile, word
        wrdfile.close()
    return cur_word
