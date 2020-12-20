import requests

import nltk

def get_top_posts(num):
    url = f"https://www.reddit.com/r/photoshopbattles/top/.json?limit={num}"

    headers = {
        'User-Agent': 'photoshopbattles autophotoshop bot',
    }

    req = requests.request("GET", url, headers=headers)
    data = req.json()
    count = data["data"]["dist"]
    def get_title(x): return data["data"]["children"][x]["data"]["title"]
    titles = [get_title(n)[10:] for n in range(0,count) if get_title(n)[:10] == "PsBattle: "]
    return titles


def noun_from_title(title):
    tokens = nltk.word_tokenize(title)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for (word, pos) in tagged if (lambda x: x == 'NN')(pos)]
    nouns.extend([word for (word, pos) in tagged if (lambda x: x[:2] == 'NN')(pos)])
    return nouns[0]
