from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length
from app.models import User

class LoginForm(FlaskForm):
  username = StringField('username', validators = [DataRequired()])
  password = PasswordField('password', validators = [DataRequired()])
  remember_me = BooleanField('remember me')
  submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators = [DataRequired()])
  email = StringField('Email', validators = [DataRequired(), Email()])
  password = PasswordField('Password', validators = [DataRequired()])
  repeat_password = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
  remember_me = BooleanField('remember me')
  submit = SubmitField('Sign In')

  def validate_username(self, username):
      user = User.query.filter_by(username = username.data).first() 
      if user is not None:
         raise ValidationError("This username already exists.")

  def validate_email(self, email):
    user = User.query.filter_by(email = email.data).first() 
    if user is not None:
        raise ValidationError("This email address is already registered.")
    

class EditProfileForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    about_me = TextAreaField("About me", validators=[Length(min=0,max=200)])
    submit = SubmitField('Submit')
