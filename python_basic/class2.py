class Flight:
	class_attr= []
	
	def __init__(self):
		self.class_attr= []
	
	def add_instance_attr(self, number):
		self.class_attr.append(number)
	
	def add_class_attr(self, number):
		Flight.class_attr.append(number)
	