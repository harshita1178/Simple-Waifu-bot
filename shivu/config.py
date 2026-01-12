class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6675050163"
    sudo_users = "8263587086", "6675050163"
    GROUP_ID = -1003582936745
    TOKEN = "8528082371:AAEXxhW34AtWI9FgzIMc4e6n4LvK6-GHHi0"
    mongo_url = "mongodb+srv://samosauchiha_db_user:ANIMELOVER11@simple.52vd62r.mongodb.net/?appName=Simple"
    PHOTO_URL = ["https://files.catbox.moe/q8t9x9.jpg", "https://files.catbox.moe/db5y3g.jpg"]
    SUPPORT_CHAT = "III_Shibuya_arc_III"
    UPDATE_CHAT = "Obsidian_Studios"
    BOT_USERNAME = "Eloise_Waifu_Bot"
    CHARA_CHANNEL_ID = "-1002781691865"
    api_id = 30878865
    api_hash = "2150ec9db8a0bf83fb4f0465c67f74eb"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
