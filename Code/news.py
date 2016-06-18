#!/usr/bin/python
import requests
import json
from datetime import date, timedelta

# function to get current news from guardian api


def getnews(current_word):
    API_KEY = open("cred_guardian.txt", "r").read().strip()
    API_ENDPOINT = 'http://content.guardianapis.com/search'
    yesterday = date.today() - timedelta(1)
    yest = yesterday.strftime('%Y-%m-%d')
    my_params = {
        'show-fields':'shortUrl',
        'from-date': yest,
        'q': current_word,
        'api-key': API_KEY
    }
    resp = requests.get(API_ENDPOINT, my_params)
    data = resp.json()
    cur_news = data['response']['results'][0]
    return(cur_news)
