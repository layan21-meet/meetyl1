class Person(object):
	def __inti__(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.food = food 
	def eat(self,food):
		print(self.name + "is drinking a smoothie")
	def mood (self):
		print(self.name + "'s mood ist scheisse")
person1 = Person("Mark",34, "Bayern", "male")
person1.eat()
person1.mood()
		



