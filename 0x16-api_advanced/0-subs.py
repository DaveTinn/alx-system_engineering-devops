#!/usr/bin/python3
'''Python Interpreter.'''

import requests


def number_of_subscribers(subreddit):
    '''Method to get the number of subscribers.'''

    # Constructing the URl for the API endpoint.
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # A custom User-Agent to avoid Too Many Requests
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by u/Wunderkind94)"
            }

    # A GET requst to Reddit's API
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get('data')
    return res.get('subscribers')
