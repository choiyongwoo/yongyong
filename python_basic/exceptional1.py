import sys
'''Exception을 설명하는 모듈'''

from math import log
def string_log(s):
	v= convert(s)
	return log(v)	

def convert(s):
	'''int로 변환'''
	try:
			a= int(s)
			print('성공')
	except (ValueError, TypeError) :
		pass
	return a