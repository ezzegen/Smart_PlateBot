from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but_open = KeyboardButton('/Режим_работы')
but_place = KeyboardButton('/Расположение')
but_menu = KeyboardButton('/Меню')
but_my_contact = KeyboardButton('Поделиться номером', request_contact=True)
but_my_location = KeyboardButton('Поделиться геолокацией', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(but_open, but_place).add(but_menu).row(but_my_contact, but_my_location)
