import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_inventory")
def get_inventory():
    inventories = list(mongo.db.inventories.find())
    return render_template("search_inventory.html", inventories=inventories)


@app.route("/search", methods=["GET", "POST"])
def search():
    # inventories = list(mongo.db.inventories.find())
    query = request.form.get("query")
    inventories = list(mongo.db.inventories.find({"$text": {"$search": query}}))
    return render_template("search_inventory.html", inventories=inventories)


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=10, max=15, message= 'Username must be between 10 and 15 Characters')])
    password = PasswordField('password', validators=[InputRequired()])



@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        # check if username already exists in db and whether validatiors have been met
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
            
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful {}!".format(request.form.get("username")))
        return redirect(url_for("profile", username=session["user"])) 
    return render_template("register.html", form=form)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                "profile", username=session["user"]))
            
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_inventory", methods=["GET", "POST"])
def add_inventory():
    if request.method == "POST":
        inventory = {
            "created_by": session["user"],
            "loudspeaker_brand": request.form.get("loudspeaker_brand"),
            "loudspeaker_product": request.form.get("loudspeaker_product"),
            "loudspeaker_product_qty": request.form.get("loudspeaker_product_qty"),
            "mixer_brand": request.form.get("mixer_brand"),
            "mixer_product": request.form.get("mixer_product"),
            "mixer_product_qty": request.form.get("mixer_product_qty"),
            "microphone_brand": request.form.get("microphone_brand"),
            "microphone_product": request.form.get("microphone_product"),
            "microphone_product_qty": request.form.get("microphone_product_qty")
        }
        mongo.db.inventories.insert_one(inventory)
        flash("Inventory Successfully Added")
    return render_template("add_inventory.html")


@app.route("/edit_inventory/<inventory_id>", methods=["GET", "POST"])
def edit_inventory(inventory_id):

    if request.method == "POST":
        submit = {
            "created_by": session["user"],
            "loudspeaker_brand": request.form.get("loudspeaker_brand"),
            "loudspeaker_product": request.form.get("loudspeaker_product"),
            "loudspeaker_product_qty": request.form.get("loudspeaker_product_qty"),
            "mixer_brand": request.form.get("mixer_brand"),
            "mixer_product": request.form.get("mixer_product"),
            "mixer_product_qty": request.form.get("mixer_product_qty"),
            "microphone_brand": request.form.get("microphone_brand"),
            "microphone_product": request.form.get("microphone_product"),
            "microphone_product_qty": request.form.get("microphone_product_qty")
        }
        mongo.db.inventories.update({"_id": ObjectId(inventory_id)}, submit)
        flash("Inventory Successfully Updated")
        return my_inventory()

    inventory = mongo.db.inventories.find_one({"_id": ObjectId(inventory_id)})
    return render_template("edit_inventory.html", inventory=inventory)


@app.route("/delete_inventory/<inventory_id>")
def delete_inventory(inventory_id):
    mongo.db.inventories.remove({"_id": ObjectId(inventory_id)})
    flash("Inventory Successfully Deleted")
    return my_inventory()



@app.route("/my_inventory")
def my_inventory():
    inventories = list(mongo.db.inventories.find())
    return render_template("my_inventory.html", inventories=inventories)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
