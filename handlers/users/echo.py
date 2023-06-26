from aiogram import types

from loader import dp, db, bot


@dp.callback_query_handler()
async def group_detail(call: types.CallbackQuery):
    group = await db.select_group(id=int(call.data))
    participants = await db.select_participants(group_id=group['group_id'], user_id=call.from_user.id)
    print(participants)
    chat = await bot.get_chat(chat_id=group['group_id'])
    await call.message.edit_text(text=f"Siz {chat.title} guruhiga {len(participants)} ta odam qo'shgansiz.")
