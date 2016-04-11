import os

from kik import KikApi, Configuration

BOT_USERNAME = os.environ.get('PEPE_BOT_USERNAME')
BOT_API_KEY = os.environ.get('PEPE_BOT_API_KEY')

IMGUR_CLIENT_ID = os.environ.get('PEPE_IMGUR_CLIENT_ID')

bot_config = {
	"username" : BOT_USERNAME,
	"key" : BOT_API_KEY
}
pepe_url = "https://api.imgur.com/3/album/U2dTR"

kik = KikApi(bot_config["username"], bot_config["key"])
