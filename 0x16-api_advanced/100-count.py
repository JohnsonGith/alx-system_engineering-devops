#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100, 'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']
        after = data['after']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title and not title.count(word.lower() + '.') and not title.count(word.lower() + '!') and not title.count(word.lower() + '_'):
                    counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())

        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            results = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in results:
                print(f'{word}: {count}')
    else:
        print('Invalid subreddit or no posts found')


