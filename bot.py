
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from plugins.config import Config

from pyrogram import Client as Ntbot
from pyrogram import filters
from plugins.youtube_dl_button import app as Client2
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Ntbot = Ntbot(
        "Uploader Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins)

  if STRING:
    apps = [Client2, Ntbot]
    for app in apps:
      idle()
      for app in apps:
        app.stop()
  else:
    Ntbot.run()


#if STRING:
    #apps = [Client2,bot]
    #for app in apps:
        #app.start()
    #idle()
    #for app in apps:
        #app.stop()
