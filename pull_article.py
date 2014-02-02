import requests
import nltk

url = 'http://www.nytimes.com'


def nltk_pulling(url):
	source = requests.get(url)
	source = source.text

	clean = nltk.clean_html(source)
	tokens = nltk.word_tokenize(clean)
	freqdist = nltk.FreqDist(tokens)
	freqdist.items()
	return freqdist.items()



def pull_freqdist(url):
	source = requests.get(url)
	source = source.text

	clean = nltk.clean_html(source)
	tokens = nltk.word_tokenize(clean)
	freqdist = nltk.FreqDist(tokens)
	return freqdist

def test_pull_freqdist(url, freqdist):
	nltk_pulling(url)
	#assert typeof(source.text)) == "class 'nltk.text.Text'"
	assert type(freqdist) == ("class 'nltk.probability.FreqDist'")

