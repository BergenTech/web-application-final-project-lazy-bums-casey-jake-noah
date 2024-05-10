import sqlite3
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def access_to_all_clubs():
    pass

def access_to_all_users():
    pass

def view_all_users():
    # db initialization
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    
    # get all users
    db_cursor.execute("SELECT * FROM users")
    data = db_cursor.fetchall()
    db.close()
    return data

def demote_leader():
    pass

def remove_user():
    pass


