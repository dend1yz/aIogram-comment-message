from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging

BOT_TOKEN = '' #Здесь указываете ваш токен бота.

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Включение логирования
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())
