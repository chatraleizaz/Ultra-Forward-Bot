import datetime
from os import environ

# Dont Remove My Credit @Silicon_Bot_Update 
# This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "27876808")
    API_HASH = environ.get("API_HASH", "414f022bf4a6620cb4bba3505605e374")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7931443175:AAEXfOF4QrmQrhPuGFSUh3Pr6lqiSOO4VU0") 
    BOT_SESSION = environ.get("BOT_SESSION", "worfdgbbbot") 
    
    # MongoDB connection and database name should be properly set
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://jauharobaid:1VAOB4Fm5gvM2YKS@cluster0.1nc4nru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    # Ensure a valid database name is set
    DATABASE_NAME = environ.get("DATABASE_NAME", "jauharobaid")  # Add a fallback default name here
    
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7098324238').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002684943176'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')

# Dont Remove My Credit @Silicon_Bot_Update 
# This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
# Dont Remove My Credit @Silicon_Bot_Update 
# This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz
