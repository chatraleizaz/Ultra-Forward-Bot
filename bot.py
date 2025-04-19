#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

import asyncio
import logging 
import logging.config
from database import db 
from config import Config  
from pyrogram import Client, __version__, idle
from pyrogram.raw.all import layer 
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait 
from aiohttp import web
from plugins import web_server 

# Configure logging
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

class Bot(Client): 
    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            bot_token=Config.BOT_TOKEN,   
            sleep_threshold=10,
            workers=200,
            plugins={"root": "plugins"}
        )
        self.logger = logger

    async def start_bot(self):
        await self.start()
        me = await self.get_me()
        self.id = me.id
        self.username = me.username
        self.first_name = me.first_name
        self.set_parse_mode(ParseMode.DEFAULT)
        
        logger.info(f"{me.first_name} | Pyrogram v{__version__} | Layer {layer} | Username: @{me.username}")
        logger.info("Bot started successfully.")

        # Start web server
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", int(Config.PORT)).start()

        # Notify users
        text = "<b>๏[-ิ_•ิ]๏ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ !</b>"
        logger.info(text)

        success = failed = 0
        users = await db.get_all_frwd()
        async for user in users:
            try:
                await self.send_message(user['user_id'], text)
                success += 1
            except FloodWait as e:
                await asyncio.sleep(e.value + 1)
                await self.send_message(user['user_id'], text)
                success += 1
            except Exception:
                failed += 1 

        if (success + failed) > 0:
            await db.rmve_frwd(all=True)
            logger.info(f"Restart messages sent | Success: {success} | Failed: {failed}")

    async def stop_bot(self):
        logger.info(f"Bot @{self.username} is shutting down...")
        await self.stop()
        logger.info("Bot stopped cleanly.")

# Main function
app = Bot()

async def main():
    try:
        await app.start_bot()
        await idle()
    except asyncio.CancelledError:
        pass
    finally:
        await app.stop_bot()

if __name__ == "__main__":
    asyncio.run(main())
