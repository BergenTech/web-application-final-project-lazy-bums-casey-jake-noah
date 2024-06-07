import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from user import *

#create admin
def make_noah_admin():
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try:
        db_cursor.execute("""UPDATE users SET isAdmin=1 WHERE email=?""", ("themostedgygamerever456@gmail.com",))
        db_cursor.execute("""UPDATE users SET isAdmin=1 WHERE email=?""", ("ceasylee@gmail.com",))
        db_cursor.execute("""UPDATE users SET isAdmin=1 WHERE email=?""", ("noahmatiaskim@gmail.com",))
        db_cursor.execute("""UPDATE users SET isAdmin=1 WHERE email=?""", ("emregemici@gmail.com",))
        db.commit()
    except Exception as e:
        db.rollback()
    db.close()


###EVENT STUFF
def approve_event(event_id):
    #change the field from false to true
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try: 
        db_cursor.execute("""UPDATE events SET isApproved = 1 WHERE id = ?""", (event_id,))
        db.commit()
    except Exception as e:
        db.rollback()
def reject_event(event_id):
    #reject the event
    #email to leaders will be sent that application has been rejected
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try: 
        db_cursor.execute("""DELETE FROM events WHERE id = ?""", (event_id,))
        db.commit()
    except Exception as e:
        db.rollback()

### CLUB STUFF
def approve_club():
    pass

def remove_club(club_id):
    #email the leaders notifying their removal
    #remove the club
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try: 
        db_cursor.execute("""DELETE FROM clubs WHERE id = ?""", (club_id,))
        db.commit()
    except Exception as e:
        db.rollback()

###USER STUFF
def promote_teacher(user_id, club_id):
    #change user from not leader to leader by inserting into teacher / leader role
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try: 
        db_cursor.execute("""INSERT INTO leaders (user_id, club_id, isTeacher) VALUES (?,?,?)""", (user_id, club_id, 1,))
        db.commit()
    except Exception as e:
        db.rollback()

def demote_leader(user_id, club_id):
    #remove user from the leader table
    pass


# MAKE SURE THE FUNCTION REMOVES FROM my_clubs, messages, events, etc (may 30)
def remove_user(user_id):
    #remove the user
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try: 
        db_cursor.execute("""DELETE FROM users WHERE id= ?""", (user_id,))
        db.commit()
    except Exception as e:
        db.rollback()


### AUTOMATED STUFF
