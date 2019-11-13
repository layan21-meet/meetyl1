class User():
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = []
		self.posts = []
	def add_friend(self, email):
		self.friends_list.append(email)
		print(self.name + 'has added' + email + 'as a friend')
	def remove_friends(self, email):
		self.friends_list.remove_friends(email)
		print(self.name + 'has removed'+ email + 'as a friend')
	def create_post(self, text):
		self.posts.append(text)
		print (self.name + 'has posted' + text)
	def get_userInfo(self):
		print("Name:" + self.name + "Email:" + self.email + "Password:" + self.password + "Friends:" + self.friends + "Posts:" + self.posts)
user1 = User("Mark","m.trommer@schmidtschule.org","trommerphysik")
user2 = User("Celine", "yaghiceline21@gmail.com","cecececec")
user1.add_friend("m.trommer@schmidtschule.org")
user2.create_post("Happpppyyy Birthdaaaaaayyy")


