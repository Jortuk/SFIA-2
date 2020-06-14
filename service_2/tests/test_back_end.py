import pytest, unittest
from unittest.mock import patch
from application import app, db
from application.models import Cuisine
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

    def test_cuisine_view(self):
        response = self.client.get(url_for('cuisine'))
        self.assertEqual(response.status_code, 200)

class TestRepr(TestBase):

    def test_cuisine_repr(self):
        c = Cuisine()
        assert c == 'Test Cuisine'
        
    @patch('application.models.Cuisine.__repr__', return_value='Test Cuisine')
    def test_cuisine_repr_mock(self, __repr__):
        self.assertEqual(__repr__(), 'Test Cuisine')