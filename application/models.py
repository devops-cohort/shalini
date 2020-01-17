from flask_login import UserMixin
from application import db, login_manager
from datetime import datetime

#relationship model, next stage in making the db see comments in Posts table
'''
photo_labels= db.Table('photo_type', db.Model.metadata,
    db.Column('postsID', db.Integer, db.ForeignKey('posts.postsID')),
    db.Column('themeID', db.Integer, db.ForeignKey('theme.themeID'))
        )
'''

#posts table
class Posts(db.Model):
    postsID = db.Column(db.Integer, primary_key=True, autoincrement = True )
    photo_link = db.Column(db.String(300), nullable = False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    continent = db.Column(db.String(100), nullable=False)
#    continent_id = db.Column(db.Integer, db.ForeignKey('continent.id'), nullable=False)
#    description = db.relationship('Theme', secondary = photo_labels, backref = db.backref('photo_theme'), lazy='dynamic')


    def __repr__(self):
        return ''.join([
            'Photo ID: ', str(self.photoID),'\r\n',
            'Photo Link ', self.photo_link, '\r\n',
            'Title: ', self.title, '\r\n',
            'Content: ', self.content, '\r\n'
            'Continent: ', self.continent
        ])

#theme tables
class Theme(db.Model):
    themeID = db.Column(db.Integer, primary_key=True, autoincrement = True)
    theme = db.Column(db.String(100), nullable=False)
  


    def __repr__(self):
        return ''.join([
            'Theme ID: ', str(self.id),'\r\n',
            'Photo Theme ', self.theme
        ])

#users table
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    posts = db.relationship('Posts', cascade = 'delete', backref = 'author', lazy=True)


    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    def __repr__(self):
        return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email])

#continent and themes table, next stage in making the db see comments in Posts table
'''
class Continent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    continent = db.Column(db.String(100), nullable=False)
    continent_posts = db.relationship('Posts', backref = 'continent', lazy=True)


    def __repr__(self):
        return ''.join([
            'Country ID: ', str(self.id),'\r\n',
            'Continent ', self.continent
        ])

class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db
    portraiture=db.Column(db.String(50), nullable=False)
    urban_landscape=db.Column(db.String(50), nullable=False)
    film=db.Column(db.String(50), nullable=False)
    flora_fauna=db.Column(db.String(50), nullable=False)
    theme_r= db.relationship('Country_Theme', backref='author', lazy=True)

'''









