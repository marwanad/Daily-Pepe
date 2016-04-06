import os
"""
Handles launching the application

"""
from flask.ext.script import Manager, Server
from app import create_app

app = create_app(os.getenv('PEPE_BOT_FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=9000))

if __name__ == '__main__':
	manager.run()
