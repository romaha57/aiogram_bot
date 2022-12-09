from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# создаем reply кнопку для отправки геопозиции
location_button = KeyboardButton(text='Отправить геопозицию', request_location=True)
all_reply_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
all_reply_keyboards.add(location_button)
