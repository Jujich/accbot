import aiogram
from dotenv import load_dotenv
load_dotenv('config.env')
import os


bot = aiogram.Bot(token=os.environ.get('TEST_TOKEN'))
