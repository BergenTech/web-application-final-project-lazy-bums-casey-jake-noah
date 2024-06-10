import sqlite3
import os
from user import *

class attendance():
    def __init__(self, id, club_id, isPresent):
        self.id = id
        self.club_id = club_id
        self.isPresent = isPresent

def get_attendance(club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    db_cursor = 

def commit_attendance(user_id, club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try:
        db_cursor.execute("""UPDATE users SET isPresent=1 WHERE user_id=? AND club_id=?""", (user_id, club_id))
        db.commit()
    except Exception as e:
        db.rollback()
    db.close()
    pass

def reset_attendance():
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try:
        db_cursor.execute("""UPDATE users SET isPresent=0""")
        db.commit()
    except Exception as e:
        db.rollback()
    db.close()
    pass