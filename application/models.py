from flask_login import UserMixin
from application import db, login_manager
from datetime import datetime


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Country ID: ', self.id, '','\r\n',
            'Country: ', self.country_name, '\r\n'
        ])





class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, '', self.last_name,
            '\r\n',
            'Title: ', self.title, '\r\n', slef.content
        ])





class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    def __repr__(self):
        return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email])



'''


class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db
    portraiture=db.Column(db.String(50), nullable=False)
    urban_landscape=db.Column(db.String(50), nullable=False)
    film=db.Column(db.String(50), nullable=False)
    flora_fauna=db.Column(db.String(50), nullable=False)
    theme_r= db.relationship('Country_Theme', backref='author', lazy=True)


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(200), nullable=False)
    photo_r= db.relationship('Country_Theme', backref='author', lazy=True)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Country_Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('Photo.id'), nullable=False)
    theme_id = db.Column(db.Integer, db.ForeignKey('Theme.id'), nullable=False)
    country_theme = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'Country Theme ID', str(self.id), '\r\n', 
            'Theme ID ', str(self.theme_id), '\r\n', 
            'Photo ID ', str(self.photo_id), '\r\n',
            ])

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(10000), nullable=False, unique=True)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    country_theme_id = db.Column(db.Integer, db.ForeignKey('Country_Theme.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'Post ID', str(self.id), '\r\n',





class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(30), nullable=False)
    last_name=db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    user_r= db.relationship('Country_Theme', backref='author', lazy=True)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n', 
            'Email: ', self.email,'\r\n',
            'Name: ', self.first_name, '', self.last_name 
        ])

'''