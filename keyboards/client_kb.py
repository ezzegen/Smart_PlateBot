from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

but_open = InlineKeyboardButton('Режим работы', callback_data='open')
but_place = InlineKeyboardButton('Расположение', callback_data='place')
but_menu = InlineKeyboardButton('Меню', callback_data='menu')

kb_client = InlineKeyboardMarkup(resize_keyboard=True)

kb_client.row(but_open, but_place).add(but_menu)
