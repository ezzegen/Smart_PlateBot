from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but_load = KeyboardButton('/Загрузить')
but_delete = KeyboardButton('/Удалить')
kb_adm = ReplyKeyboardMarkup(resize_keyboard=True)
kb_adm.add(but_load).add(but_delete)

but_cancel = KeyboardButton('/Отмена')
kb_adm_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_adm_cancel.add(but_cancel)
