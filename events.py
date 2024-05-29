import sqlite3
import csv
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
def create_event(club_id, event_content, event_start_date, event_end_date, event_tags, people_interested):
    pass
## EVENT EDITING FUNCTIONS (needs to do before approval)
def edit_event(event_content, event_start_date, event_end_date, event_tags, people_interested):
    pass

###EVENT APPROVAL FUNCTIONS 
def approve_event(event_id):
    pass

#### EVENT SEARCHING FUNCTIONS
def search_event():
    pass