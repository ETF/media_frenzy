import requests
import nltk

url = 'http://www.nytimes.com'
source = requests.get(url)
source = source.text

clean = nltk.clean_html(source)
tokens = nltk.word_tokenize(clean)
freqdist = nltk.FreqDist(tokens)
freqdist.items()