from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from create_bot import bot
from keyboards.client_kb import kb_client


async def process_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Напишите ему: '
                            'https://t.me/Smart_PlateBot')
        await message.delete()


async def restaurant_open(message: types.Message):
    await bot.send_message(message.from_user.id, 'Режим работы:\nПн-Пт с 08:00 до 21:00\n'
                                                 'Сб-Вс с 10:00 до 01:00')


async def restaurant_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Печорская, д.5', reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start, commands=['start', 'help'])
    dp.register_message_handler(restaurant_open, commands='Режим_работы')
    dp.register_message_handler(restaurant_place, commands='Расположение')
