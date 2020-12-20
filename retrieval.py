import requests

import spacy
nlp = spacy.load('en_core_web_sm')

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
    doc = nlp(title)
    nps = [chunk for chunk in doc.noun_chunks]
    return nps[0].root
