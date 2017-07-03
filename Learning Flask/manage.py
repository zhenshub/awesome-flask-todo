from flask_script import Manager,Server
from app import *
from app.models import Todo

manager = Manager(app)
server = Server(host='0.0.0.0', port=5000, use_debugger=True, use_reloader=True)


@manager.command
def app_did_start():
    print('\nserver start!!!\n')


@manager.command
def save_todo():

    todo = Todo(content='mb')
    todo.save()


manager.add_command("runserver", server)
if __name__ == '__main__':
    manager.run()