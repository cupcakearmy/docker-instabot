import os
import time
import json

from src import InstaBot

data = json.load(open('config.json'))
data['database_name'] = 'data.db'
data['session_file'] = 'data.session'
bot = InstaBot(**data)

bot.mainloop()