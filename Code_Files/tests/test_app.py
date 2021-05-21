# Import the necessary modules
#from flask.wrappers import Response
from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import Player


class TestBase(TestCase):
    def create_app(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
        app.config["SECRET_KEY"] = "ANYTHING"
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBU"] = True
        
        return app
    
    def setUp(self):
        db.create_all()

        test_player1 = Player(name="test player 1", id=1)
        test_player2 = Player(name="test player 2", id=2)
        
        db.session.add(test_player1)
        db.session.add(test_player2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):

    def test_home_page_get(self):
        response = self.client.get(url_for('index'))
        print(response.data)
        self.assertIn(b"test player 1", response.data)
        self.assertEqual(response.status_code, 200)

    def test_add_player(self):
        response = self.client.post(url_for('add'), data={"name":"Test Player Name"})
        self.assertIn(b"Test Player Name", response.data)

    def test_delete_player(self):
        response = self.client.get(url_for("delete", id=1))
        num_players = Player.query.count()
        self.assertEqual(num_players, 1)