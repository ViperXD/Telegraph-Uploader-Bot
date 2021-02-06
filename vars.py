import os

class Config(object):
    # Get a token from @BotFather
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    
    # Get these values from my.telegram.org
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]
