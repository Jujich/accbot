from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot import bot
from strings.start_strings import start_strings

router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    msg = await bot.send_message(
        chat_id=message.from_user.id,
        text=start_strings["welcome_string"]
    )
    await state.update_data(menu_id=msg.message_id)
