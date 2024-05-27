from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextInput, TextArea, SubmitInput


class CustomTextInput(TextInput):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("class", "form-control")
        return super().__call__(field, **kwargs)


class CustomTextArea(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("class", "form-control")
        return super().__call__(field, **kwargs)


class CustomSubmitInput(SubmitInput):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("class", "btn btn-primary")
        return super().__call__(field, **kwargs)


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], widget=CustomTextInput())
    email = StringField(
        "Email", validators=[DataRequired(), Email()], widget=CustomTextInput()
    )
    message = TextAreaField(
        "Message", validators=[DataRequired()], widget=CustomTextArea()
    )
    submit = SubmitField("Send", widget=CustomSubmitInput())
