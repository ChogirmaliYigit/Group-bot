from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot

async def groups_markup(groups):
    markup = InlineKeyboardMarkup(row_width=1)
    for group in groups:
        try:
            print(group['id'])
            chat = await bot.get_chat(chat_id=group['group_id'])
            markup.insert(InlineKeyboardButton(text=chat.title, callback_data=group['id']))
        except Exception as error:
            print(error)
    return markup
