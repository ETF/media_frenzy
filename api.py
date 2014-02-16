import requests
import nltk
from stop_words import sw 

url = ""

def counts_pages_words(url):
	source = requests.get(url)
	clean = nltk.clean_html(source.text)
	tokens = nltk.word_tokenize(clean) #can make class nltk.text.Text object out of tokens
	tokens = [word for word in tokens if word not in sw]
	freqdist = nltk.FreqDist(tokens)
	return { "title": source.url.title, "freq_dist": freqdist.items() }