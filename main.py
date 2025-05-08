import asyncio
from aiogram import Dispatcher, Bot
from bots import bot_client, bot_accountant

# Accountant
from routers.Accountant import start as start_a

# Client
from routers.Client import start as start_c


dp_acc = Dispatcher()
dp_client = Dispatcher()


async def run_bot(dp: Dispatcher, bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def main():
    # Acc
    dp_acc.include_routers(start_a.router)

    # Client
    dp_client.include_routers(start_c.router)

    await asyncio.gather(
        run_bot(dp_client, bot_client),
        run_bot(dp_acc, bot_accountant)
    )


if __name__ == '__main__':
    try:
        print("Bot running...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Terminated')
