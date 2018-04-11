import os
import time
import json

from src import InstaBot

data = json.load(open('config.json'))
bot = InstaBot(**data)

while True:
	bot.new_auto_mod()