from aiogram import Bot
import os
from dotenv import load_dotenv
load_dotenv(".env")

bot_client = Bot(token=os.environ.get('CLIENT_TOKEN'))
bot_accountant = Bot(token=os.environ.get('ACCOUNTANT_TOKEN'))
