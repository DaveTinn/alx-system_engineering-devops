#!/usr/bin/python3
'''Python Interpreter.'''

import requests


def top_ten(subreddit):
    '''
    Function to query the Reddit API and
    prints the titles of the first 10 hot posts.
    '''
    request = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"limit": 10},
    )

    if request.status_code == 404:
        for res in request.json().get("data").get("children"):
            hot_post = res.get("data")
            title = hot_post.get("title")
            print(title)
    else:
        print(None)
