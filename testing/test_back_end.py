import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Users

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MY_SQL_USER'))+':'+str(getenv('MY_SQL_PASSWORD'))+'@'+str(getenv('MY_SQL_URL'))+'/'+str(getenv('MY_SQL_DB'))        )
        return app



    def setUp(self):
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")

        # save users to database
        db.session.add(admin)
        db.session.commit()


    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestApplication(TestBase):

    def test_login_view(self):
        '''
        testing the home page is accessible without login
        '''
        reponse = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)



