from flask import Flask
from mongoengine import *

app = Flask(__name__)
app.config.from_object("config")
connect('localDB')


from app import views, models

