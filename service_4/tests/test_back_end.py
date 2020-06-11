import pytest, unittest

from application import app, db
from application.models import Chow
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        config_name = 'test'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
            SECRET_KEY=getenv('TEST_SECRET_KEY'),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_chow_view(self):
        response = self.client.post(
            url_for('chow'),
            data=dict(
                cuisine = "Mexican",
                dessert = "Chocolate Mousse"
            ),
        )
        self.assertIn(b"Mexican", response.data)