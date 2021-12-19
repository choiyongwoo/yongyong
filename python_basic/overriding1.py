class Country:
	'''Super Class'''
	
	name= '국가명'
	population= '인구'
	capital= '수도'
	
	def show(self):
		print('국가 클래스의 메서드입니다.')
	
class Korea(Country):
	'''Sub Class'''
	
	def __init__(self, name, population, capital):
		self.name= name
		self.population= population
		self.capital= capital
	
	def show(self):
		super().show()
		print('국가의 이름은{} \n국가의 인구는 {} \n 국가의 수도는 {}'.format(self.name, self.population, self.capital))
		