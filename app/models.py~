#class Post:
	#def __init__(self, title, author, content): #the initialization method
		#self.title = title   #Defining the title attribute
		#self.author = author #Defining the author attribute
		#self.content = content #Defining the content attribute


from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key =True)
	firstname = db.Column(db.String(65))
	lastname = db.Column(db.String(65))
	username = db.Column(db.String(120), unique = True)
	post = db.relationship('Post', backref = 'author')


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100))
	content = db.Column(db.Text)
	author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
