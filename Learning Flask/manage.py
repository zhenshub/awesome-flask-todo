from flask_script import Manager,Server
from app import app

manager = Manager(app)
server = Server(host='0.0.0.0', port=5000, use_debugger=True, use_reloader=True)

@manager.command
def app_did_start():
    print('\nserver start!!!\n')

manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()