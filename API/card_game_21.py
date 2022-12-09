import json
from json import JSONDecodeError

import requests

from utils.bkackjack_game_params import pretty_card_suit_and_value

deck_id = ''


def get_first_card() -> str:
    """Отправляет гет запрос для получения новой колоды карт"""

    url = 'https://deckofcardsapi.com/api/deck/new/draw/?count=1'
    response = requests.get(url)
    deck = json.loads(response.text)
    global deck_id
    deck_id = deck["deck_id"]
    card = deck["cards"][0]["code"]

    pretty_card = pretty_card_suit_and_value(card)

    return pretty_card


def get_more_one_card() -> (str, bool):
    """Функция отрабатывает, когда пользователь нажимает на кнпоку 'еще'
    и мы берем еще 1 карту из колоды"""

    url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1'
    response = requests.get(url)
    try:
        deck = json.loads(response.text)

    # если ошибка декодирования json, то возвращаем False и
    # пишем пользователю о недоступности сервера
    except JSONDecodeError:
        return False

    # получаем карту из колоды и преобразуем ее вид
    card = deck["cards"][0]["code"]
    pretty_card = pretty_card_suit_and_value(card)

    return pretty_card
