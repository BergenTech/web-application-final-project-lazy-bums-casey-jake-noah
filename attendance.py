import sqlite3
import os
from user import *

class attendance():
    def __init__(self, id, club_id, isPresent):
        self.id = id
        self.club_id = club_id
        self.isPresent = isPresent
#this is for the initial members

def check_is_present(user_id, club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #get all attendance from a clubId
    db_cursor.execute("""SELECT * FROM attendance WHERE user_id=? AND club_id = ? AND isPresent=1""",(user_id, club_id))
    data = db_cursor.fetchone()
    db.close()
    return data

def get_attendance_from_club(club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #get all attendance from a clubId
    db_cursor.execute("""SELECT * FROM attendance WHERE club_id=?""",(club_id,))
    data = db_cursor.fetchall()
    db.close()
    return data

def commit_attendance(user_id, club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try:
        #check if the person exists first in attendance:
        person_exists = check_is_present(user_id, club_id)
        if person_exists:
            db_cursor.execute("""UPDATE attendance SET isPresent=1 WHERE user_id=? AND club_id=?""", (user_id, club_id,))
        else:
            db_cursor.execute("""INSERT INTO attendance (user_id,club_id, isPresent) VALUES (?,?,?)""", (user_id, club_id, 1,))
        print("success")
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