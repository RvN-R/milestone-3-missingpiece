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
import sys
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
    # Function renders index.html
    return render_template("index.html")


@app.route("/get_inventory")
def get_inventory():
    # Function returns a list of all the items found in Monogo DB collection
    # Assigns results to a variable called inventories.
    # Renders search_inventory.html.
    inventories = list(mongo.db.inventories.find())
    return render_template("search_inventory.html", inventories=inventories)


@app.route("/search_passive")
def search_passive():
    # Function renders search_passive.html
    return render_template("search_passive.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    # Function searches Mongo DB collection using a varaible called query
    # Assigns result of that search to inventories variable
    # Repeats search using varaible called query and returns "created_by" data
    # Assigns result of that search to created_by variable
    # Searches Mongo DB users collection
    # For data matching created_by variable
    # Zips "users" and "inventories" and assigns to variable called boxes
    # renders serach_inventory.html
    if request.method == "POST":
        query = request.form.get("query")
        inventories = list(mongo.db.inventories.find(
            {"$text": {"$search": query}}))
        created_by = list(mongo.db.inventories.find(
            {"$text": {"$search": query}}, {"created_by": 1}))
        users = []
        for i in created_by:
            users.append((mongo.db.users.find_one(
                {"username": i.get("created_by")})))
        return render_template(
            "search_inventory.html", inventories=inventories, boxes=zip(
                users, inventories))


class RegistrationForm(FlaskForm):
    # uses FlaskForm to create username and password variables
    username = StringField(
        'username', validators=[InputRequired(), Length(
            min=10, max=15,
            message='Username must be between 10 and 15 Characters')])
    password = PasswordField('password', validators=[InputRequired()])


@app.route("/register", methods=["GET", "POST"])
def register():
    # Function renders register.html
    # Takes data from HTML form and inserts it to Mongo DB users
    # collection.
    # existing_user variable cross checks username with users collection.
    # Returns user to profile page if
    # The form isn't successfully filled out correctly.
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        # check if username already exists in db and whether validatiors have
        # been met
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "company_name": request.form.get("company_name"),
            "street_name": request.form.get("street_name"),
            "postcode": request.form.get("postcode"),
            "city": request.form.get("city"),
            "phone": request.form.get("phone")
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful {}!".format(
            request.form.get("company_name")))
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html", form=form)


class LoginForm(FlaskForm):
    # uses FlaskForm Validators to confirm log in is correct
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])


@app.route("/login", methods=["GET", "POST"])
def login():
    # Function renders login.html
    # existing_user variable cross checks username with users collection
    # If it finds a match then checks password using FlaskForm Validators
    form = LoginForm()
    if request.method == "POST" and form.validate():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Function searches users collection in Mongo DB.
    # If user is in session.
    # Assigns results to varaible called companies
    # Renders profile.html and data from companies variable
    # Else it returns flash message and redirects
    if "user" in session:
        companies = list(mongo.db.users.find())
        return render_template("profile.html", companies=companies)
    else:
        flash("You must be logged in to perform that action")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Function removes user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_inventory", methods=["GET", "POST"])
def add_inventory():
    # Function renders add_inventory.html
    # If user is in session.
    # Inserts data from inventory variable to inventories collection
    # Categories varible returns data from categories collection
    # Else it returns flash message and redirects
    if "user" in session:
        if request.method == "POST":
            inventory = {
                "created_by": session["user"],
                "categories_name": request.form.get("categories_name"),
                "brand": request.form.get("brand"),
                "product": request.form.get("product"),
                "product_qty": request.form.get("product_qty")
            }
            mongo.db.inventories.insert_one(inventory)
            categories = mongo.db.categories.find().sort("categories_name", 1)
            flash("Inventory Successfully Added")
            return render_template("add_inventory.html", categories=categories)

        categories = mongo.db.categories.find().sort("categories_name", 1)
        return render_template("add_inventory.html", categories=categories)
    else:
        flash("You must be logged in to perform that action")
        return redirect(url_for("login"))


@app.route("/edit_inventory/<inventory_id>", methods=["GET", "POST"])
def edit_inventory(inventory_id):
    # Function searches inventories collection for data that matches _id
    # If user is in session.
    # Assigns results to variable inventory
    # Searches categories collection
    # Assigns results to varibale categories
    # Renders edit_inventory
    # If recieves a POST request function inserts data from submit variable
    # to inventories collection and updates collection.
    # Else it returns flash message and redirects
    if "user" in session:
        inventory_entry = mongo.db.inventories.find_one(
            {"_id": ObjectId(inventory_id)})
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if user == inventory_entry.get("created_by"):
            if request.method == "POST":
                submit = {
                    "created_by": session["user"],
                    "categories_name": request.form.get("categories_name"),
                    "brand": request.form.get("brand"),
                    "product": request.form.get("product"),
                    "product_qty": request.form.get("product_qty")
                }
                mongo.db.inventories.update(
                    {"_id": ObjectId(inventory_id)}, submit)
                flash("Inventory Successfully Updated")
                return my_inventory()

            inventory = mongo.db.inventories.find_one(
                {"_id": ObjectId(inventory_id)})
            categories = mongo.db.categories.find().sort("categories_name", 1)
            return render_template(
                "edit_inventory.html",
                inventory=inventory, categories=categories)
        else:
            flash("You are not authorsied to perform this action")
            return redirect(url_for("my_inventory"))
    else:
        flash("You must be logged in to perform that action")
        return redirect(url_for("login"))


@app.route("/edit_company_address/<company_id>", methods=["GET", "POST"])
def edit_company_address(company_id):
    # Function searches users collection for data that matches _id
    # If user is in session.
    # Assigns results to variable company
    # Returns list from users collection and assigns to companies variable
    # Renders edit_company_address.html
    # If recieves post request, updates users collection with submit variable
    # Returns to profile.html
    # Else it returns flash message and redirects
    if "user" in session:
        company_info = mongo.db.users.find_one({"_id": ObjectId(company_id)})
        print(company_info)
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        print(user)
        if user == company_info.get("username"):
            if request.method == "POST":
                submit = {"$set": {
                    "company_name": request.form.get("company_name"),
                    "street_name": request.form.get("street_name"),
                    "postcode": request.form.get("postcode"),
                    "city": request.form.get("city"),
                    "phone": request.form.get("phone")
                }}
                mongo.db.users.update({"_id": ObjectId(company_id)}, submit)
                companies = list(mongo.db.users.find())
                flash("Company Details Updated")
                return render_template(
                    "profile.html", company=company_id, companies=companies)

            company = mongo.db.users.find_one({"_id": ObjectId(company_id)})
            companies = list(mongo.db.users.find())
            return render_template(
                "edit_company_address.html", company=company,
                companies=companies)
        else:
            flash("You are not authorised to perfom this action")
            return redirect(url_for("profile", username=session["user"]))
    else:
        flash("You must be logged in to perform that action")
        return redirect(url_for("login"))


@app.route("/delete_inventory/<inventory_id>")
def delete_inventory(inventory_id):
    # Function removes data matching _id from inventories collection
    # returns to my_inventory function
    mongo.db.inventories.remove({"_id": ObjectId(inventory_id)})
    flash("Inventory Successfully Deleted")
    return my_inventory()


@app.route("/my_inventory")
def my_inventory():
    # Function returns list of inventories collection
    # If user is in session.
    # Assigns results to inventories variable
    # Renders my_inventory.html and inventories variable
    # Else it returns flash message and redirects
    if "user" in session:
        inventories = list(mongo.db.inventories.find())
        return render_template("my_inventory.html", inventories=inventories)
    else:
        flash("You must be logged in to perform that action")
        return redirect(url_for("login"))

if __name__ == "__main__":
    # If __name__ is equal to __main__ runs app
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
