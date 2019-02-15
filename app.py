# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config.from_pyfile('config.py')


modus = Modus(app)

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run()