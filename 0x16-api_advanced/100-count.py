#!/usr/bin/python3
"""Python Interpreter."""

import requests


def count_words(subreddit, word_list, word_count=[], page_after=None):
    """
    Recursive function to query the Reddit API,
    Parse the title of all hot articles, and
    Prints a sorted count of given keywords.
    """
    headers = {"User-Agent": "HolbertonSchool"}

    word_list = [word.lower() for words in word_list]

    if bool(word_count) is False:

