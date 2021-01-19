from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional

class AddPet(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired("Pet Name is required")])
    species = StringField("Species", validators = [InputRequired(message ="Species required")])
    url = StringField("Photo URL", validators = [Optional()])
    age = IntegerField("Age", validators = [InputRequired("Age required")])
    notes = StringField("Notes", validators = [Optional()])


class EditPet(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired("Pet Name is required")])
    species = StringField("Species", validators = [InputRequired(message ="Species required")])
    url = StringField("Photo URL", validators = [Optional()])
    age = IntegerField("Age", validators = [InputRequired("Age required")])
    notes = StringField("Notes", validators = [Optional()])
    available = BooleanField("Available?")