class User(object):
	def __init__(self,name,email,password,friends_list,posts):
		self.friends_list = []
		self.posts = []
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = []
		self.posts = []
	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name+" has added "+email+" as a friend")
	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name+" has removed "+email+" from friends")
	def create_post(self,text):
		self.posts.append(text )
		print(self.name+" has posted "+ text)
		post1 = Post("post", self.name)
	def get_userinfo(self):
		print("Name:"+self.name)
		print("Email:"+self.email)
		print("Password:"+self.password)
		print("Friends:"+str(self.friends_list))
		print("Posts:"+str(self.posts))
class Post(object):
	def __init__(self,name,caption,comments=[]):
		self.name = name
		self.caption = caption
		self.comments = []

	def add_caption(self,text):
		self.caption = text 
		print(self.name + " has added a caption " + self.caption)
	def add_comment(self,caption_text):
		self.comment_text = comment_text
		self.comment.append(comment_text)
		print(self.name + " has added a comment " + comment_text)
	def like_post(self):
		print(self.name + " has liked your post!")

class Comment(Post):
	pass
login = input("login or sign up?")
if login =="sign up":
	name1 = input("Please enter an email")
	email = input("Birthday Date")


user1 = User("Layan","layann.hamdan@gmail.com","LaYan2019",0,0)
user2 = User("Celine","Celine@gmail.com","Hibaaa9102",0,0)
user1.add_friend("Hiba22@gmail.com")
user2.create_post("Happyyy place")
user1.get_userinfo()
user2.get_userinfo()
user1.remove_friend("Hiba22@gmail.com")
post1 = Post("layan", "Pizzzzaa Love","comment")
post1.add_caption("hhiiiiiiiiiiiiiiiiiii")

