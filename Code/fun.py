#!/usr/bin/python
from replacements import dic


def modnews(headline):
    for i, j in dic.iteritems():
        headline = headline.replace(i, j)
    return headline
