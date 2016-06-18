#!/usr/bin/python
import sys
from randwords import getcurrentword
from news import getnews
from fun import modnews
from bot import tweet
today_news = []
current_word = getcurrentword()
if current_word is None:
    sys.exit()
else:
    today_news = getnews(current_word)
    headline = today_news['webTitle']
    url = today_news['fields']['shortUrl']
    new_headline = modnews(headline)
    msg = str(new_headline + " [ " + url+" ]")
    tweet(msg)
    print "tweet done"
