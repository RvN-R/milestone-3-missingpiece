import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_inventory")
def get_inventory():
    inventory = mongo.db.loudspeaker_systems.find()
    return render_template("inventory.html", inventories=inventory)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=10, max=15, message= 'Username must be between 10 and 15 Characters')])
    password = PasswordField('password', validators=[InputRequired()])

@app.route("/register", methods=["GET", "POST"])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        return "Your Account Has Been Created"
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
