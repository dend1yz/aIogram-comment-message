from aiogram import types
from bot import dp, bot
import logging

WELCOME_MESSAGE = "" #Здесь вставляете ваше приветственное сообщение.
WELCOME_IMAGE_URL = "" #Здесь вставляете приветственную картинку.
CHAT_LINK = "" #Здесь вставляете ссылку на ваш чат.
RULES_LINK = "" #Здесь вставляете ссылку на правила.

@dp.message_handler(content_types=types.ContentTypes.ANY, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def send_welcome(message: types.Message):
    if message.is_automatic_forward:
        keyboard = types.InlineKeyboardMarkup()
        chat_button = types.InlineKeyboardButton(text="Чат", url=CHAT_LINK)
        rules_button = types.InlineKeyboardButton(text="Правила", url=RULES_LINK)
        keyboard.add(chat_button, rules_button)

        await bot.send_photo(chat_id=message.chat.id, photo=WELCOME_IMAGE_URL, caption=WELCOME_MESSAGE, reply_markup=keyboard, reply_to_message_id=message.message_id)
        logging.info(f'Отправил приветственное сообщение к ID посту: {message.message_id}') #Если он отправил вам это сообщение. Значит он работает.
