from dotenv import load_dotenv
import os
load_dotenv()
bot_name = os.getenv("BOT_NAME")
print("Welcome! I am", bot_name)