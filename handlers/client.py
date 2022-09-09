from aiogram import types, Dispatcher
from create_bot import dp, bot


@dp.message_handler(commands=['start', 'help'])
async def process_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Напишите ему: '
                            'https://t.me/Smart_PlateBot')
        await message.delete()


@dp.message_handler(commands='Режим_работы')
async def restaurant_open(message: types.Message):
    await bot.send_message(message.from_user.id, 'Режим работы:\nПн-Пт с 08:00 до 21:00\n'
                                                 'Сб-Вс с 10:00 до 01:00')


@dp.message_handler(commands='Расположение')
async def restaurant_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Печорская, д.5')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start, commands=['start', 'help'])
    dp.register_message_handler(restaurant_open, commands='Режим_работы')
    dp.register_message_handler(restaurant_place, commands='Расположение')
