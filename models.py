from google.appengine.ext import db

class User(db.Model): #This is the model for a user. / jk
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

class Post(db.Model):
    title = db.StringProperty(required = True)
    body = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    # TODO - we need an author field here; it should be required
    # See the last Flick-List for an example of how to do this. Remember from Flick-list that
    # post.author points to a full user class. To just get author's name, you need to do
    # post.author.username to make your structure point to a username. / jk
    author = db.ReferenceProperty(User, required = True)
