from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_game_button():
    more_one_card = InlineKeyboardButton(text='ещё', callback_data='more_one_card')
    again = InlineKeyboardButton(text='начать заново', callback_data='again')
    open_hand = InlineKeyboardButton(text='вскрываемся', callback_data='open_hand')

    card_game_button = InlineKeyboardMarkup(row_width=2)
    card_game_button.add(more_one_card, again, open_hand)

    return card_game_button
