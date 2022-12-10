from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_inline_button_menu():
    """Создаем inline кнопки для функций: погоды, перевода текста,
    мотивационных цитат и игра в блекджек"""

    weather_button = InlineKeyboardButton(text='🌤 Погода', callback_data='weather')
    translation_button = InlineKeyboardButton(text='📖 Перевод', callback_data='translation')
    motivation_button = InlineKeyboardButton(text='🔝 Мотивационная цитата знаменитости',
                                             callback_data='motivation')
    card_game_21 = InlineKeyboardButton(text='🃏 Сыграть в 21', callback_data='card_game')

    all_inline_button = InlineKeyboardMarkup(row_width=2)
    all_inline_button.add(weather_button, translation_button, motivation_button, card_game_21)

    return all_inline_button
