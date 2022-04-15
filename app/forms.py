# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description =TextAreaField('Description', validators=[DataRequired()], description='Please enter the message you would like to send.')
    photo = FileField('Photo Upload', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Images only!')], description='Please select an Image to upload')