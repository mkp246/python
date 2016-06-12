'''Retrieve and Print words form A URL

Usage:
	Python withs.py <URL>
'''
from urllib.request import urlopen
import sys


def fetch_words(url):
	'''Fetch a list of words form URL
	
	Args:
		url: The Url of UTF-8 text document

	Returns:
		A list of list containing words in a
		line of the document
	'''
	with urlopen(url) as story:
			story_words = []
			for line in story:
				line_words = line.decode('utf-8').split()
				story_words.append(line_words)
	return story_words


def print_words(story_words):
	'''Print an item per line'''
	for word in story_words:
		for v in word:
			print(v)


def main(url):
	'''Print each word from a text document form URL'''
	print_words(fetch_words(url))


if __name__ == '__main__':
	main(sys.argv[1]);