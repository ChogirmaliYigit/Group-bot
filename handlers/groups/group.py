from loader import db, dp, bot
from aiogram import types
from filters.group import IsGroup
from aiogram.dispatcher.filters.builtin import CommandStart



@dp.message_handler(IsGroup(), CommandStart())
async def start_group(message: types.Message):
    chat = message.chat
    group_admins = await bot.get_chat_administrators(chat.id)
    # for admin in group_admins:
    #     if admin.user.id == chat.id:
    await message.answer(text=f"ishladi")
