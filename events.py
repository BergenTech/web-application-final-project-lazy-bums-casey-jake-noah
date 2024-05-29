import sqlite3
import os
from user import *

class Event():
    def __init__(self, id, club_id, event_title, event_content, event_start_date, event_end_date, event_tags, people_interested, isApproved):
        self.id = id
        self.club_id = club_id
        self.event_title = event_title
        self.event_content = event_content
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.event_tags = event_tags
        self.people_interested = people_interested
        self.isApproved = isApproved
#### BEFORE APPROVAL
## EVENT CREATION FUNCTIONS
def create_event(club_id, event_title, event_content, event_start_date, event_end_date, event_tags):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()

    new_event = Event(None, club_id, event_title, event_content, event_start_date, event_end_date, event_tags)

    try: 
        db_cursor.execute(
            """INSERT INTO events
            (event_title, event_content, event_start_date, event_end_date, event_tags, club_id) VALUES (?,?,?,?,?,?)""",
            (new_event.even_title, new_event.event_content, new_event.event_start_date, new_event.event_end_date, new_event.event_tags, new_event.club_id,)
        )
        db.commit()
        print('successful!')
    except Exception as e:
        db.rollback()
## EVENT EDITING FUNCTIONS (needs to do before approval)
def edit_event(event_content, event_start_date, event_end_date, event_tags):
    pass

###EVENT APPROVAL FUNCTIONS 
def approve_event(event_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try: 
        db_cursor.execute("""UPDATE clubs SET isApproved = TRUE WHERE id = ?""", (event_id,))
        db.commit()
        print('successful!')
    except Exception as e:
        db.rollback()

#### EVENT SEARCHING FUNCTIONS
def search_event():
    pass