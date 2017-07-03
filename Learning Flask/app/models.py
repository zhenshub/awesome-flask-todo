from mongoengine import *
from flask_wtf.form import FlaskForm
import datetime


class Todo(Document):
    content = StringField(required=True, max_length=20)
    time = DateTimeField(default=datetime.datetime.now())
    status = IntField(default=0)

    # def __init__(self, content, time, status, *args, **kwargs):
    #     super(Document, )
    #     self.content = content
    #     self.time = time
    #     self.status = status

