class Country:
	'''Super Class'''
	
	name= '국가명'
	population= '인구'
	capital= '수도'
	
	def show(self):
		print('국가 클래스의 메서드입니다.')
	
class Korea(Country):
	'''Sub Class'''
	
	def __init__(self, name):
		self.name= name
	
	def show_name(self):
		print('국가 이름은:', self.name)
		