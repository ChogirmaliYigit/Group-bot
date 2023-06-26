from loader import db, dp, bot
from aiogram import types
from filters.group import IsGroup
from aiogram.dispatcher.filters.builtin import CommandStart



@dp.message_handler(IsGroup(), CommandStart())
async def start_group(message: types.Message):
    chat = message.chat
    group_admins = await bot.get_chat_administrators(chat.id)
    bot_me = await bot.get_me()
    print(bot_me)
    for admin in group_admins:
        if admin.user.id == bot_me.id:
            group = await db.select_group(group_id=chat.id)
            if group:
                await message.answer(text=f"{chat.title} guruhi oldin bazaga qo'shilgan!")
            else:
                await db.add_group(group_id=chat.id)
                await message.answer(text=f"{chat.title} guruhi bazaga muvaffaqiyatli qo'shildi!")


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    for item in message:
        if item[0] == "new_chat_participant":
            participant_id = item[1].get('id')
    participants = await db.select_participants(user_id=message.from_user.id, group_id=message.chat.id)
    for participant in participants:
        if participant_id and participant_id != participant['participant_id']:
            await db.add_participant(group_id=message.chat.id, user_id=message.from_user.id, participant_id=participant_id)
