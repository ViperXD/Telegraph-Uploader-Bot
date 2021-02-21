import os

class Config(object):
    # Get a token from @BotFather
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    
    # Get these values from my.telegram.org
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]
    
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(os.environ.get("TIME_LIMIT"))

    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
