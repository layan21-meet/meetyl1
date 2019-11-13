class Parrot:
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color

	def fly(self):
		print(self.name + " is flying")


parrot1 = Parrot("Mike", 7, "Green")
parrot2 = Parrot("Charlie", 5, "Red")
print(parrot1.name, parrot1.age)
parrot1.fly()
parrot2.fly()
parrot1.name = "Celine"
print(parrot1.name)