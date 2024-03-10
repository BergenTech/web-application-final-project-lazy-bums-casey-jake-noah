from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.utils import secure_filename
import csv
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_mail import Mail
from flask_mail import Message
from flask_login import LoginManager, UserMixin
from flask_login import login_user, current_user, logout_user, login_required
import random
import base64
from cryptography.fernet import Fernet
import user

app = Flask(__name__)
#main page
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/clubs')
def clubs():
    pass
@app.route('/events')
def events():
    pass
@app.route('/my_clubs')
def my_clubs():
    pass

if __name__ == "__main__":
    app.secret_key = ""  # Change this to a secure ENCRYPTED key
    app.run(debug=True)