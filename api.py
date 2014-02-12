import requests
import nltk


def counts_pages_words(url):
	source = requests.get(url)
	clean = nltk.clean_html(source.text)
	tokens = nltk.word_tokenize(clean) #can make class nltk.text.Text object out of tokens
	freqdist = nltk.FreqDist(tokens)
	freqdist.items()
	return { "title": source.url.title, "freq_dist": freqdist.items() }