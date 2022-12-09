from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_game_button():
    more_one_card = InlineKeyboardButton(text='ещё', callback_data='more_one_card')
    again = InlineKeyboardButton(text='начать заново', callback_data='again')

    card_game_button = InlineKeyboardMarkup(row_width=2)
    card_game_button.add(more_one_card, again)

    return card_game_button
