from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired#, ValidationError

# from application.models import Player

class PlayerForm(FlaskForm):
    
    name = StringField('Name', validators = [DataRequired()])
    position_id = StringField('Postion' )
    submit = SubmitField('Save Name')
    



class PositionForm(FlaskForm):
    position = SelectField("Select Position", 
        choices=[
            ("Goalkeeper", "GK"), ("Defender", "DEF"), 
            ("Midfielder", "MID"), ("Attacker", "ATT")
        ]
    )
    submit = SubmitField('Save Position')