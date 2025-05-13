from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from strings.accountant_strings import accountant_strings
from bots import bot_accountant as bot
import os
from orm.api import create_accountant

router = Router()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await message.answer(
        accountant_strings['start']
    )
    await state.set_state('reg1')


@router.message(StateFilter('reg1'))
async def get_name(message: Message, state: FSMContext):
    await bot.edit_message(
        chat_id=message.from_user.id,
        message_id=message.message_id,
        text=accountant_strings['reg1'].substitute(
            username=message.text
        ),
    )
    await state.set_state('reg2')


@router.message(StateFilter('reg2'))
async def get_name(message: Message, state: FSMContext):
    password = os.environ.get('ACCOUNTANT_PASSWORD')
    if message.text == password:
        await bot.edit_message(
            chat_id=message,
            message_id=message.message_id,
            text=accountant_strings['reg2']
        )
        await state.clear()
        await create_accountant(
            message.from_user.id,
            message.from_user.username
        )
    else:
        await bot.edit_message(
            chat_id=message.from_user.id,
            message_id=message.message_id,
            text=accountant_strings['reg2_fail']
        )
