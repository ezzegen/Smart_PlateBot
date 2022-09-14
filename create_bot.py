from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

stg = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=stg)
