from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired

# from application.models import Player

class PlayerForm(FlaskForm):
    
    name = StringField('Name', validators = [DataRequired()])
    position_id = StringField('Postion' )
    submit = SubmitField('Save Name')
    

class PositionForm(FlaskForm):
    position = SelectField("Select Position", 
        choices=[
            ("Goalkeeper", "Goalkeeper"), ("Defender", "Defender"), 
            ("Midfielder", "Midfielder"), ("Attacker", "Attacker")
        ]
    )
    submit = SubmitField('Save Position')

# class PositionForm(FlaskForm):
#     position = SelectField("Select Position", 
#         choices=[
#             ("Goalkeeper", "Goalkeeper"), ("Defender", "Defender"), 
#             ("Midfielder", "Midfielder"), ("Attacker", "Attacker")
#         ]
#     )
#     submit = SubmitField('Save Position')