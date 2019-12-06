from flask_login import UserMixin
from application import db, login_manager
from datetime import datetime



#photo_labels= db.Table('photo_type', db.Model.metadata,
#    db.Column('postsID', db.Integer, db.ForeignKey('posts.postsID')),
#    db.Column('themeID', db.Integer, db.ForeignKey('theme.themeID'))
#        )

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
            'Content: ', self.content
        ])


class Theme(db.Model):
    themeID = db.Column(db.Integer, primary_key=True, autoincrement = True)
    theme = db.Column(db.String(100), nullable=False)
  


    def __repr__(self):
        return ''.join([
            'Theme ID: ', str(self.id),'\r\n',
            'Photo Theme ', self.theme
        ])

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
'''


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






'''

    def __repr__(self):
        return ''.join([
            'Post ID: ', str(self.id), '\r\n',
            'User: ', self.first_name,'\r\n', ' ', self.last_name,
            'Title: ', self.title, '\r\n',
            'Content: ', self.content, '\r\n'
            'Photo: ', self.photo_link, '\r\n',
            'Theme: ', self.theme_posts, '\r\n',
            'Continent: ', self.continent_posts
        ])











class Continent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    continent=db.Column(db.String(50), nullable=False)
    continent_post__relationship= db.relationship('Continent', backref='author', lazy=True)


    def __repr__(self):
        return ''.join([
            'Continent ID: ', self.id, '','\r\n',
            'Continent: ', self.continent, '\r\n'
        ])





class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name,'\r\n', ' ', self.last_name,
            'Title: ', self.title, '\r\n', 
            'Content: ', self.content, '\r\n'
            'Continent: ', self.continent_id
        ])





class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Posts')
    
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    def __repr__(self):
        return ''.join([
            'Username: ', self.first_name,'\r\n', ' ', self.last_name, 
            'Email: ', self.email,
        ])






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
