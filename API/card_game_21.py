import requests
import json

from utils.bkackjack_game_params import pretty_card_suit_and_value

deck_id = ''


def get_first_card() -> (str, bool):
    """Отправляет гет запрос для получения новой колоды карт"""

    url = 'https://deckofcardsapi.com/api/deck/new/draw/?count=1'
    response = requests.get(url)
    deck = json.loads(response.text)
    global deck_id
    deck_id = deck["deck_id"]
    card = deck["cards"][0]["code"]

    pretty_card = pretty_card_suit_and_value(card)

    return pretty_card


def get_more_one_card() -> str:
    """Функция отрабатывает, когда пользователь нажимает на кнпоку 'еще'
    и мы берем еще 1 карту из колоды"""

    url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1'
    response = requests.get(url)
    deck = json.loads(response.text)
    card = deck["cards"][0]["code"]
    pretty_card = pretty_card_suit_and_value(card)

    return pretty_card
