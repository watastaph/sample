from flask_app.config.mysqlconnection import MySQLConnection

class Posts:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.posts = data['posts']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



