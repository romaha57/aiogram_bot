from aiogram import Dispatcher

from states.trans_state import TranslateText
from handlers.start_help_handler import start_help
from handlers.echo_handler import echo
from handlers.weather_handler import press_weather_button, get_weather_from_api
from handlers.translate_handler import press_translation_button, get_translation_text
from handlers.motivation_quote_handler import press_motivation_button
from handlers.blackjack_game_handler import press_start_or_again_card_game, \
    press_one_more_card, press_open_hand_card_game


def register_handlers(dp: Dispatcher) -> None:
    """Функция для регистрации всех хендлеров"""

    dp.register_message_handler(start_help, commands=['start', 'help'])
    dp.register_callback_query_handler(press_weather_button, text='weather')
    dp.register_message_handler(get_weather_from_api, content_types=['location'])
    dp.register_callback_query_handler(press_translation_button, text='translation')
    dp.register_callback_query_handler(press_motivation_button, text='motivation')
    dp.register_callback_query_handler(press_start_or_again_card_game, text='card_game')
    dp.register_callback_query_handler(press_one_more_card, text='more_one_card')
    dp.register_callback_query_handler(press_start_or_again_card_game, text='again')
    dp.register_callback_query_handler(press_open_hand_card_game, text='open_hand')
    dp.register_message_handler(get_translation_text, state=TranslateText.text)
    dp.register_message_handler(echo, content_types=['text'])
