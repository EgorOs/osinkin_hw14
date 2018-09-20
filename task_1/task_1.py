from flask import Flask
from requests import get
from bs4 import BeautifulSoup
import re

app = Flask('__main__')
SITE_NAME = 'https://flask-dance.readthedocs.io/en/latest/proxies.html'

INVISIBLE_ELEMS = ('style', 'script', 'head', 'title')
RE_SPACES = re.compile(r'\s{3,}')
TM_SYMBOL = '\u2122'.encode('utf-8').decode('utf-8')


def visible_texts(soup):
    """ get visible text from a document """
    text = ' '.join([
        s for s in soup.strings
        if s.parent.name not in INVISIBLE_ELEMS
    ])
    # collapse multiple spaces to two spaces.
    return RE_SPACES.sub('  ', text)


def add_symbols(words, text):
    for word in list(words):
        text = text.replace(word, word + TM_SYMBOL)
    return text


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):

    # Get page content
    result = get('{}{}'.format(SITE_NAME, path)).content
    soup = BeautifulSoup(result, 'html.parser')

    # Get readable text, strip tags
    texts = visible_texts(soup)

    # Strip symbols
    words = re.sub(r'[^\w]', ' ', texts)

    # Get words of interest
    long_words = {w for w in words.split(' ') if len(w) >= 10}

    # Add symbols to source code
    source_html = soup.prettify()
    edited_html = add_symbols(long_words, source_html)

    data = str(edited_html).encode('utf-8')
    return data


app.run(host='0.0.0.0', port=8000)
