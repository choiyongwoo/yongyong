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
	except (ValueError, TypeError) as e:
		print('에러 정보:', e, file=sys.stderr)
		raise ValueError('Argument에 잘못된 값이 전달되었습니다')
	else:
		print('에러가 발생하지 않았어요!')
	finally:
		print('여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.')
	return a
