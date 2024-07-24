import sqlite3
import os
from datetime import datetime
from user import *

class attendance():
    def __init__(self, id, club_id, isPresent):
        self.id = id
        self.club_id = club_id
        self.isPresent = isPresent
#this is for the initial members

def check_if_present_day(user_id, club_id, date_present):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #get all attendance from a clubId
    #get the current date
    db_cursor.execute("""SELECT * FROM attendance WHERE user_id=? AND club_id = ? AND date_present=?""",(user_id, club_id, date_present))
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
        current_date = str(datetime.now().date())
        db_cursor.execute("""INSERT INTO attendance (user_id,club_id, date_present) VALUES (?,?,?)""", (user_id, club_id, current_date,))
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