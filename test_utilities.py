import unittest
from utilities import pull_info, nltk_pulling, pull_freqdist, pull_source

URL1 = "http://www.nytimes.com"
URL2 = "http://www.cnn.com"
URL3 = "http://wwww.sfgate.com"
URL4 = "http://www.foxnews.com/"
URL5 = "http://www.washingtonpost.com/"

ALL_URL = [URL1, URL2, URL3, URL4, URL5]


#REMINDER: ALL html MUST BE .lowered()

class TestPullInfo(unittest.TestCase):
	def test_pull_info(self):
		urls1 = pull_info(URL1)
		self.assertEqual(urls1[0:2], (u'HTTP://WWW.NYTIMES.COM/', 'http://www.nytimes.com'))
	def test_pull_info_https_fail(self):
		url1 = pull_info(URL1)
		self.assertEqual(url1[0:2], (u'HTTPS://WWW.NYTIMES.COM/', 'http://www.nytimes.com'))

	def test_html_doctype(self):
		url1 = pull_info(URL1)
		self.asserEqual(url1[2][:15], (u'<!DOCTYPE html>'))

	def test_each_html_doctype(self):
		for url in ALL_URL:
			url = pull_info(url)
			self.assertEqual(url[2][:15].lower(), (u'<!doctype html>'))
			#note this is simply checking the string at the top of the doc and the request object probly already handles that
			#this will fail, take foxnews.com for example

	def test_eng_lang(self):
		for url in ALL_URL:
			url = pull_info(url)
			#note below that 'lang="en-US"' is lowered9) manually
			assert(('lang="en"' or 'lang="en-us"') in url[2][:1000].lower())
			#not sure how to write the above python code

class TestNltkPulling(unittest.TestCase):
	def test_nltk_pulling_type(self):
		for url in ALL_URL:
			pulled = nltk_pulling(url)
			self.assertEqual(str(type(pulled[1])), "<type 'list'>")
	def test_nltk_substantial_pulling_data(self):
		for url in ALL_URL:
			pulled = nltk_pulling(url)
			assert(pulled[1][0][1] > 5)
	def test_nltk_pulling_slash_us(self):
		for url in ALL_URL:
			pulled = nltk_pulling(url)
			for p in pulled:				
				assert("/u" not in p[1][0])


class TestPullFreqDist(unittest.TestCase):
	def test_pull_freqdist(self):
		#COULD DO: assert typeof(source.text)) == <type 'unicode'> 
		#or throw the Text class on there "class 'nltk.text.Text'"
		#note that below we have to make each TYPE a string to escape the CLASS keyword
		self.assertEqual(str(type(pull_freqdist(URL1))), ("<class 'nltk.probability.FreqDist'>"))

class TestPullSource(unittest.TestCase):
	def test_pull_source(self):
		self.assertEqual(str(type(pull_source(URL1))), ("<type 'unicode'>"))


def show_each_html_hundred_chars(urls):
		for url in ALL_URL:
			url = pull_info(url)
			print(url[0], url[2][:100])