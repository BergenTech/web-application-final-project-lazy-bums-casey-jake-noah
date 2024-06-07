import sqlite3
import os
from user import *

class attendance():
    def __init__(self, id, club_id, isPresent):
        self.id = id
        self.club_id = club_id
        self.isPresent = isPresent
