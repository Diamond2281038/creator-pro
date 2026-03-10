import time
from bot_manager import restart_bot

def watchdog(bots):

    while True:

        for bot in bots:
            restart_bot(bot)

        time.sleep(3600)
