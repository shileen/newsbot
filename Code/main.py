#!/usr/bin/python
import sys
from randwords import getcurrentword
from news import getnews
from fun import modnews
from bot import tweet
from refill import refill

today_news = []
current_word = getcurrentword()
if current_word is None:
    refill()

current_word = getcurrentword()
today_news = getnews(current_word)
headline = today_news['webTitle']
url = today_news['fields']['shortUrl']
new_headline = modnews(headline)
msg = str(new_headline + " [ " + url + " ]")
tweet(msg)
print "tweet done"
