#!/usr/bin/python
def refill():
    fo = open("words.txt", "w")
    words = ["murder", "debate"]
    for word in words:
        print>>fo, word

    fo.close()
