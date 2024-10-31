from aiogram import Dispatcher
from routes import start

dp = Dispatcher()
dp.include_routers(*[
    start.router,
]) # import and add routers here
