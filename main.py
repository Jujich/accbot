import asyncio
from bot import bot
from dispatcher import dp


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("Bot running...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down...")
