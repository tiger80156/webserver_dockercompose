import requests
import os
from flask import render_template, request
from controllers import blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from .db import mysqlInstance

class CameraForm(FlaskForm):
    Username = StringField("Username", validators=[DataRequired()])
    Password = StringField("Password", validators=[
                          DataRequired(), Length(min=7, max=20)])
    submit = SubmitField('Submit')


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = CameraForm()
    return render_template("index.html", form=form)

@blueprint.route("/create", methods=["POST"])
def createUser():
    username = request.form.get("Username")
    password = request.form.get("Password")
    mysqlInstance.NewUser(username, password)

    return render_template("createSuccess.html")