from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

builder = InlineKeyboardBuilder()
builder.row(
    InlineKeyboardButton(
        text="Добавить",
        callback_data="add_group",
        url="https://t.me/buh4biz_acc_bot?startgroup=newgroups&admin=manage_chat+change_info+delete_messages+restrict_members+invite_users+promote_members"
    ),
)
add_bot_kb = builder.as_markup()
