import aiogram
from dotenv import load_dotenv
load_dotenv('config.env')
import os
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode


bot = aiogram.Bot(
    token=os.environ.get('TEST_TOKEN'),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
