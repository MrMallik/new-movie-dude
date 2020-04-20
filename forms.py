from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class filmForm(FlaskForm):
    favMovie = StringField('favMovie', validators = [DataRequired(), 
                            Length(min=2, max=20)])
    
    submit = SubmitField('Submit')