class User(object):
	def __init__(self,name,email,password,friends_list,posts):
		self.friends_list = []
		self.posts = []
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = friends_list
		self.posts = posts
   	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name+" has added "+email+" as a friend")
    def remove_friend(self,email):	
		self.friends_list.remove(email)
 		print(self.name+" has removed "+email+" as a friend")
    def post(self,text):
		self.posts.append(text)
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
	def add_caption(self,caption_text):
		self.caption_text = caption_text
		self.caption.append(caption_text)
		print(self.name + " has added the caption " + caption_text)
	def add_comment(self, comment_text):
		self.comment_text = comment_text
		self.comment.append(comment_text)
		print(self.name + " has added a comment " + comment_text)
	def like_post(self):
		print(self.name + " has liked your post!")
user1 = User("Layan","layann.hamdan@gmail.com","LaYan2019",0,0)
user2 = User("Hiba","Hiba22@gmail.com","Hibaaa9102",0,0)
user1.add_friend(user2.email)
user1.post("Hi")
user1.get_userinfo()
user1.remove_friend(user2.email)
user1.post("a new post")


