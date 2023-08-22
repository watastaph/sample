from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import posts
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Users:
    def __init__ (self, data):
        self.id =  data['id']
        self.author = data['author']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts  = []

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['txt-author']) < 3:
            flash("Author must be at least 3 characters long!")
        if not EMAIL_REGEX.match(user['txt-email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['txt-password']) < 5:
            flash("Password must be at least 5 characters long!")
        if user["txt-password"] != user["txt-cpassword"]:
            flash("Password not match!")
        return is_valid


    @classmethod
    def get_all_user(cls):
        query = "SELECT * FROM users;"
        results = MySQLConnection("vlog").query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
            #print(user)
        return users
    
    @classmethod 
    def get_all_post(cls):
        query = "SELECT * FROM users INNER JOIN posts ON users.id = posts.user_id;"
        results = MySQLConnection("vlog").query_db(query)
        posts = []
        for post in results:
            data = {
                "post_id":post["posts.id"],
                "user_id":post["id"],
                "author":post["author"],
                "date_published":post["posts.created_at"],
                "posts": post["posts"]
            }
            posts.append(data)
        print(posts)
        return posts
    
    @classmethod
    def login_user(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = MySQLConnection("vlog").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    
    @classmethod
    def retrieve_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = MySQLConnection("vlog").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def add_user(cls,data):
        query=("INSERT INTO users (author, email, password) VALUES (%(author)s, %(email)s, %(password)s); ")
        return MySQLConnection("vlog").query_db(query, data)
    
    @classmethod
    def add_post(cls,data):
        query=("INSERT INTO posts (user_id, posts) VALUES (%(user_id)s, %(posts)s); ")
        return MySQLConnection("vlog").query_db(query, data)

    @classmethod
    def delete_user(cls,data):
        query=("DELETE FROM users WHERE id = %(id)s ;")
        return MySQLConnection("vlog").query_db(query, data)
    
    @classmethod
    def update_user(cls,data):
        query=("UPDATE users SET author=%(author)s, email=%(email)s, password=%(password)s WHERE id = %(id)s ;")
        return MySQLConnection("vlog").query_db(query, data)