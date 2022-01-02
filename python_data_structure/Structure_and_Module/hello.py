hello= 'hello'
def world():
	return 'world'
if __name__=='__main__':
	print('{0} 직접 실행'.format(__name__))
else:
	print('{0} 임포트됨'.format(__name__))
