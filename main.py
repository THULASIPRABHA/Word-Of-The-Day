import requests
from datetime import date
import re
today = date.today()
fdate = date.today().strftime('%Y/%B %d')
title="Wiktionary:Word of the day/"+ fdate
S = requests.Session()
URL = "https://en.wiktionary.org/w/api.php"
params={
        'action': 'query',
        'format': 'json',
        'titles': title,
        'prop': 'revisions',
        'rvprop': 'content',
        "formatversion":"2",
   }
R = S.get(url=URL, params=params)
DATA = R.json()


pages=DATA['query']['pages'][0]['revisions'][0]['content']

wiki = re.compile(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]')
w=wiki.sub(r'\1', pages)
print(w)
