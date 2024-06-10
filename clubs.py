import sqlite3
import csv
import os
from user import *
#need to use for NOAH cus the * import is messed up 
from user import search_user
#create the club class just for some parity with sqlalchemy. Will serve useful when creating a club.
class Club():
    #initialize club object with its parameters
    #future parameters: google classroom code(?)
    def __init__(self, id, faculty_name, club_name, club_description, meeting_location, meeting_days):
        self.id = id
        self.faculty_name = faculty_name
        self.club_name = club_name
        self.club_description = club_description
        self.meeting_location = meeting_location
        self.meeting_days = meeting_days

#csv parsing functions
def parse_csv_data(csv_file):
    reader = csv.reader(csv_file)
    headers = next(reader)
    data = [row for row in reader]
    return data

def add_csv_data_to_database(file):
    csv_data = parse_csv_data(file)
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    for club in csv_data:
        try:
            new_club = Club(None, club[0], club[1], club[2], club[3], club[4])
            
            db_cursor.execute(
                """INSERT INTO clubs
                (faculty_name, club_name, club_description, meeting_location, meeting_days) VALUES (?,?,?,?,?)""",
                (new_club.faculty_name, new_club.club_name, new_club.club_description, new_club.meeting_location, new_club.meeting_days)
            )
            db.commit()
        except Exception as e:
            db.rollback()
    db.close()

#create my clubs class for the clubs the user adds
class My_Clubs():
    def __init__(self, id, user_id, clubs_id):
        self.id = id
        self.user_id = user_id
        self.clubs_id = clubs_id
      

#initialize official clubs using club list from official 2324 club list
def initialize_clubs():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, 'init', '2324ClubList.csv')
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        add_csv_data_to_database(file)

#### CLUB SEARCHING AND GETTING
#get all clubs by a sql query
def get_all_clubs():
    #db intialization
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #get all clubs
    db_cursor.execute("SELECT * FROM clubs")
    data = db_cursor.fetchall()
    db.close()
    return data

#search for club by name
def search_clubs(name):
    #db intialization
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor() 
    #prepared statement to prevent sql injection    
    db_cursor.execute("SELECT * FROM clubs WHERE club_name LIKE ?", ('%' + name + '%',))
    data = db_cursor.fetchall()
    db.close()
    return data

def search_club_by_id(id):  
    #db intialization
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor() 
    #prepared statement to prevent sql injection    
    db_cursor.execute("SELECT * FROM clubs WHERE id = ?", (id,))
    data = db_cursor.fetchall()
    db.close()
    return data

#search users of a club
def search_users_of_a_club(id):
    #db intialization
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor() 
    #prepared statement to prevent sql injection    
    db_cursor.execute("SELECT user_id FROM my_clubs WHERE club_id = ?", (id,))
    data = db_cursor.fetchall()
    users = []
    #get the username
    for user_id in data:
        users.append(get_user_by_id(user_id[0]))
    db.close()
    return users

def search_userids_of_a_club(id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    db_cursor.execute("SELECT user_id FROM my_clubs WHERE club_id = ?", (id,))
    data = db_cursor.fetchall()
    return data

# change the club logo
def change_logo(image_data, id, mime_type):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    db_cursor.execute("""UPDATE clubs 
                      SET logo = ?, mime_type = ?
                      WHERE id=? """, 
                      (image_data,mime_type,id,))
    db.commit()
    db.close()


##### USER CLUB STUFF
#need to pass user parameters of user id, club id, and later on if there is edit functionality?
def add_club_to_user(user_id, club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #add to the my_clubs table
    try: 
        db_cursor.execute(
                    """INSERT INTO my_clubs
                    (user_id, club_id) VALUES (?,?)""",
                    (user_id, club_id)
        )
        db.commit()
    except Exception as e:
        db.rollback()
    db.close()

def remove_club_to_user(user_id, club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #add to the my_clubs table
    try: 
        db_cursor.execute(
                    """DELETE FROM my_clubs
                    WHERE user_id=? AND club_id=?""",
                    (user_id, club_id)
        )
        db.commit()
    except Exception as e:
        db.rollback()
    db.close()

def user_club_exists(user_id, club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #search for my_clubs where user_id is the user_id specified
    db_cursor.execute("SELECT * FROM my_clubs WHERE user_id = ? AND club_id = ?", (user_id, club_id,))
    data = db_cursor.fetchall()
    db.close()
    return data 

def get_user_clubs(user_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #search for my_clubs where user_id is the user_id specified
    db_cursor.execute("SELECT * FROM my_clubs WHERE user_id = ?", (user_id,))
    data = db_cursor.fetchall()
    db.close()
    return data

####CLUB MANAGEMENT FUNCTIONS
def invite_leader(user_id, club_id):
    #grab the previous string in the column for owners in the club and add it onto the list
    #check if the user is already an owner
    #add the user id onto a list
    #process the list back into a string
    #insert in the clubs table
    pass

##TEMPORARY FOR DEMO! DELETE BC VERY BAD!
#make the user
def give_teacher_initial_leadership():
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    try:
        #call the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(current_directory, 'init', '2324ClubList.csv')
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_data = parse_csv_data(file)
            #parse the teachers into emails
            
            for club in csv_data:
                db_cursor.execute("""UPDATE clubs SET leaders = ? WHERE id= ? """, (jake_user_id, jake_club,))
    except IndexError:
        pass
#this is the demo to verify that once I register I am able to be an owner of specific club (ex. code club)
def make_jake_owner():
    commands = []
    #search the user table for jake's email
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #find jake
    try:
        jake_user_id = search_user("ceasylee@gmail.com")[0][0]
        jakes_clubs = get_user_clubs(jake_user_id)
        jakes_clubs = [clubs[2] for clubs in jakes_clubs]
        for jake_club in jakes_clubs:
    #enumerate using a for loop for all the club_ids specified
    #grant jake ownership 
            db_cursor.execute("""UPDATE clubs SET leaders = ? WHERE id= ? """, (jake_user_id, jake_club,))

        jake_user_id = search_user("noahmatiaskim97@gmail.com")[0][0]
        jakes_clubs = get_user_clubs(jake_user_id)
        jakes_clubs = [clubs[2] for clubs in jakes_clubs]
        for jake_club in jakes_clubs:
            db_cursor.execute("""UPDATE clubs SET leaders = ? WHERE id= ? """, (jake_user_id, jake_club,))

        db.commit()
        db.close()
    except IndexError:
        pass
    #process the user_id to a string

    #search for jake's club

    #give jake the admin access to the clubs he joined

# check if you are club owner of a specific club
def is_club_owner(user_id, club_id):
    db = sqlite3.connect('db/database.db')
    db_cursor = db.cursor()
    #grab the owner ids from the club using club_id

    data = db_cursor.fetchall()
    db.close()
    #enumerate and check if user_id matches one of the club_ids
    #if it does, return true
    #if it doesnt, return false
    return data

#this is when the app is verified (NEEDS TO BE AUTOMATIC)
def grant_ownership_access_to_teacher():
    #enumerate teacher names and prepare them as owners once they register
    pass