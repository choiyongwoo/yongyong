#module에서 작성된 파일에 function 적용
'''
	URL로부터 파일을 가져와 단어를 print 함.
Usage:
	
	
	python words.py<URL>
'''

from urllib.request import urlopen

import sys
def fetch_words():
	'''
	url주소에서 파일을 가져와 단어 리스트를 반환
	:param url: 불러올 url
	:return:
	'''
	with urlopen('https://suwoni-codelab.com/assets/story.txt') as story:
		story_words= []
		for line in story:
			line_words= line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words
	
def print_words(story_words):
	'''
	items를 print
	:param items:
	:return:
	'''
	for word in story_words:
		print(word)
		
def main():
	'''
	url을 받아 단어를 print함
	:param url:url
	:return:
	'''
	words= fetch_words()
	print_words(words)
	
if __name__=='__main__':
	main()