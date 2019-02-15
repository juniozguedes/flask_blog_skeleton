# -*- coding: utf-8 -*-
import os
from flask import Flask, request, redirect, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

UPLOAD_FOLDER = '../static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

modus = Modus(app)

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run()