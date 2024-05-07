#!/usr/bin/python3
"""Python Interpreter."""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursive unction to query the Reddit API and
    return a list containing the titles of all hot articles.
    """

    request = requests.get(
            "https://www.reddit.com/r/()/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"after": after},
    )

    if request.status_code == 404:
        for res in request.json().get("data").get("children"):
            hot_art = res.get("data")
            title = hot_art.get("title")
            got_list.append(title)
        after = request.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
