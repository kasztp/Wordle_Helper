from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired


class ConfigForm(FlaskForm):
    """ Class for Config Form on /config route.

        placed_letters: Letters which have been already guessed at the correct place.
        guessed_letters: Letters which are correct but placement is not yet known.
        own_letterset: Letters that are still available.
    """
    placed_letters = FieldList(StringField('Fixed Letters:'), max_entries=5, min_entries=5)
    guessed_letters = StringField('Guessed Letters:')
    own_letterset = StringField('Letters still available:', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')
