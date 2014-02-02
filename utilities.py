import requests
import nltk

url = 'http://www.nytimes.com'

def pull_info(url):
	news_story = requests.get(url)
	title = news_story.url.upper()
	content = news_story.text
	return (title, url, content)
	#return { "title": title, "url": url, "content" : content }

def nltk_pulling(url):
	source = requests.get(url)
	source = source.text

	clean = nltk.clean_html(source)
	tokens = nltk.word_tokenize(clean)
	freqdist = nltk.FreqDist(tokens)
	freqdist.items()

	return (url, freqdist.items())



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

