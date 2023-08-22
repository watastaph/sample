from flask import render_template, request, redirect, session
from flask_app.models.users import Users
from flask_app import app
from flask_bcrypt import Bcrypt        
from flask import flash

bcrypt = Bcrypt(app)  

#registration page
@app.route("/register")
def register():
    users = Users.get_all_user()
    posts = Users.get_all_post()
    return render_template("registration.html", all_users = users, all_posts = posts)

#login page
@app.route("/login")
def login():
    return render_template("login.html")

#verify login
@app.route("/login_user", methods=["POST"])
def login_user():
    data = {"email":request.form["txt-email"]}
    user_in_db = Users.login_user(data)
    if not user_in_db:
        flash ("Invalid Email/Password")
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["txt-password"]):
        flash ("Invalid Email/Password")
        return redirect("/login")
    session["author"] = user_in_db.author
    session["user_id"] = user_in_db.id
    return redirect("/register")

#insert record
@app.route("/add_user", methods=["POST"])
def add_user():
    if not Users.validate_user(request.form):
        return redirect('/register')
    
    pw_hash = bcrypt.generate_password_hash(request.form["txt-password"])
    data={
        "author": request.form["txt-author"],
        "email": request.form["txt-email"],
        "password": pw_hash
    }
    Users.add_user(data)
    return redirect("/register")

@app.route("/add_post", methods=["POST"])
def add_post():
    data={
        "posts": request.form["txt-post"],
        "user_id": session["user_id"]
    }
    Users.add_post(data)
    return redirect("/register")

#delete record
@app.route("/delete_user/<id>")
def delete_user(id):
    data={
        "id":id
    }
    Users.delete_user(data)
    return redirect("/register")

#retrieve record
@app.route("/retrieve_user/<id>")
def retrieve_user(id):
    data={
        "id":id
    }
    user = Users.retrieve_user(data)
    return render_template("update.html", all_user = user)

#update record
@app.route("/update_user", methods=["POST"])
def update_user():
    pw_hash = bcrypt.generate_password_hash(request.form["txt-password"])

    data={
        "author": request.form["txt-author"],
        "email": request.form["txt-email"],
        "password": pw_hash,
        "id": request.form["txt-id"]
    }
    Users.update_user(data)
    return redirect("/register")

