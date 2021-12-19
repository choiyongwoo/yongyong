#파이썬 메서드의 첫번째 파라미터명은 관례적으로 self라는 이름 사용
#호출 시 호출한 객체 자신이 전달되기 때문에 self라는 이름을 사용
#이를 이용하여 클래스에서 바로 메서드로 접근하면서 위에서 할당한 Flight의 객체 f를
#파라미터로 전달함으로써 똑같은 결과값

#생성자로 객체생성을 호출 받으면 먼저 __new__를 호출하여 객체를 생성 할당하고,
#__new__메서드가 __init__메서드를 호출하여 객체에서 사용할 초기값들을 초기화함
#일반적으로 파이썬에서 클래스를 만들 시 __init__ 메서드만
#오버라이딩 하여 객체 초기화에만 이용

class Flight:
	
#__new__메서드는 자동으로 실행되므로 제거
#__init__ 메서드에 코드 수정
#self._number로 할당했는데 변수명의 _의 의미는
#내부적으로 사용되는 변수, 파이썬기본 키워드와 충돌을 피하기 위한 변수	
	def __init__(self, number):
		if not number[:2].isalpha():
			raise ValueError('첫 두글자가 알파벳이 아님')
		if not number[:2].isupper():
			raise ValueError('첫 두글자가 대문자가 아님')
		if not number[2:].isdigit():
			raise ValueError('세번째 글자 이상이 양의 숫자가 아님')
		self.__number= number
				
	def number(self):
		return self.__number
