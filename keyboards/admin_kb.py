from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but_load = KeyboardButton('/Загрузить')
but_delete = KeyboardButton('/Удалить')
but_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)
but_case_admin.add(but_load).add(but_delete)

but_cancel = KeyboardButton('/Отмена')
but_cancel_pack = ReplyKeyboardMarkup(resize_keyboard=True)
but_cancel_pack.add(but_cancel)
