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

def check_if_already_present(club_id, date_present):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #get all attendance from a clubId
    #get the current date
    db_cursor.execute("""SELECT * FROM attendance WHERE club_id = ? AND date_present=?""",(club_id, date_present))
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

def commit_attendance(club_id, members):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try:
        #process the club form data as a list and cast to a string
        members = ' '.join(members)
        #check if the person exists first in attendance:
        current_date = str(datetime.now().date())
        check_if_alr = check_if_already_present(club_id, current_date)
        if check_if_alr: 
            db_cursor.execute("""UPDATE attendance SET users=? WHERE club_id=?""", (members,club_id))
        else: 
            db_cursor.execute("""INSERT INTO attendance (users, date_present, club_id) VALUES (?,?,?)""", (members, current_date, club_id,))
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