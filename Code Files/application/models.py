from sqlalchemy.orm import backref, relationship
from application import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Column

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    # club = db.relationship('Clubs', backref='playerclub')
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'))

# class Clubs(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     club = db.Column(db.String(30))
#     player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)


class Positions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(12))
    player = db.relationship('Player', backref='position')
    


class Squad(db.Model):
    id = db.Column(db.Integer, primary_key=True)