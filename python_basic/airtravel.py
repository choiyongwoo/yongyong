#pylint:disable=E0001
class Flight:
		
#파이썬 메서드의 첫번째 파라미터명은 관례적으로 self라는 이름 사용
#호출 시 호출한 객체 자신이 전달되기 때문에 self라는 이름을 사용
#이를 이용하여 클래스에서 바로 메서드로 접근하면서 위에서 할당한 Flight의 객체 f를
#파라미터로 전달함으로써 똑같은 결과값

#생성자로 객체생성을 호출 받으면 먼저 __new__를 호출하여 객체를 생성 할당하고,
#__new__메서드가 __init__메서드를 호출하여 객체에서 사용할 초기값들을 초기화함
#일반적으로 파이썬에서 클래스를 만들 시 __init__ 메서드만
#오버라이딩 하여 객체 초기화에만 이용

	def __init__(self):
		print('init')
		super().__init__()
	
	def __new__(cls):
		print('new')
		return super().__new__(cls)
		
	def number(self):
		return 'SN060'
		