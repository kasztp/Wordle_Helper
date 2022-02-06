from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired


class ConfigForm(FlaskForm):
    placed_letters = FieldList(StringField('Fixed Letters:'), max_entries=5, min_entries=5)
    guessed_letters = StringField('Guessed Letters:')
    own_letterset = StringField('Letters to test:', validators=[DataRequired()])
    submit = SubmitField('Send')
