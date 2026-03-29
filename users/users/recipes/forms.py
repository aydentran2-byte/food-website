from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', 
        validators=[DataRequired(), Length(min=1, max=100)])
    content = TextAreaField('Content', 
        validators=[DataRequired()])
    submit = SubmitField('Post')

class RecipeForm(FlaskForm):
    title = StringField('Recipe Title', 
        validators=[DataRequired(), Length(min=2, max=100)])
    ingredients = TextAreaField('Ingredients', 
        validators=[DataRequired()])
    instructions = TextAreaField('Cooking Instructions', 
        validators=[DataRequired()])
    prep_time = StringField('Prep Time', 
        validators=[Length(max=50)])
    cook_time = StringField('Cook Time', 
        validators=[Length(max=50)])
    servings = StringField('Servings', 
        validators=[Length(max=20)])
    submit = SubmitField('Post Recipe')
