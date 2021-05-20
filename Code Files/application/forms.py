from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
#from wtforms import validators
from wtforms.validators import DataRequired, ValidationError

from application.models import Player

class PlayerForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    submit = SubmitField('Save Name')

    position = SelectField("Select Position", choices=[("Goalkeeper", "GK"), ("Defender", "DEF"), ("Midfielder", "MID"), ("Attacker", "ATT")])
    submit = SubmitField('Save Position')

    def validate_task(self, name):
        all_players = Player.query.all()
        if name.data in all_players:
            raise ValidationError('You already have this player')

class PositionForm(FlaskForm):
    position = SelectField("Select Position", choices=[("Goalkeeper", "GK"), ("Defender", "DEF"), ("Midfielder", "MID"), ("Attacker", "ATT")])
    submit = SubmitField('Save Position')