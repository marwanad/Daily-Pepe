from flask import Flask
from config import config

# Creates an application instance based on the configuration provided
def create_app(configuration):
	app = Flask(__name__)
	app.config.from_object(config[configuration])
	
	from .bot import bot
	app.register_blueprint(bot)

	config[configuration].init_app(app)

	return app
