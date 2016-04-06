"""
	Stores the Flask application configurations
"""

class Config(object):
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

class ProductionConfig(Config):
	# custom prod config will be added here
	pass

config = {
	'development' : DevelopmentConfig,
	'production' : ProductionConfig,
	'default' : DevelopmentConfig
}
