from random import randint
from typing import Tuple


suits_card = {'S': '♠', 'D': '♦', 'C': '♣', 'H': '♥'}
values_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               '0': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
high_card = {'J': 'валет', 'Q': 'королева', 'K': 'король', 'A': 'туз'}


deck_on_hand = 0  # моя рука
random_rival_hand = 0  # рука компьютера


def pretty_card_suit_and_value(card: str) -> str:
    """Преобразует значение карты в красивый вид"""

    value = card[0]
    suit = card[1]

    # преобразуем значение карты в красивый вид
    pretty_value = values_card[value] if value not in high_card \
        else f'{high_card[value]} ({str(values_card[value])})'

    # преобразуем масть в красивый вид
    pretty_suit = suits_card[suit]

    return f'{pretty_value} {pretty_suit}'


def add_card_in_hands(card=None) -> int:
    """Добавляет значение карт к значениям в руке"""

    # берем значения глобальных переменных для своей руки и руки компьютера
    global deck_on_hand, random_rival_hand
    if card:
        card_params = card.split()

        if len(card_params) == 2:
            value = int(card_params[0])
        else:
            # если карта валет, дама, король, туз
            value = int(card_params[1].strip('()'))

        deck_on_hand += value
        random_rival_hand += randint(2, 11)

    return deck_on_hand


def check_win_or_lose() -> Tuple[str, int]:
    """Проверяет исход игры"""

    global deck_on_hand, random_rival_hand
    if (deck_on_hand == 21 and random_rival_hand != 21) or \
            (random_rival_hand < deck_on_hand < 21) or (deck_on_hand < 21 < random_rival_hand):

        deck_on_hand = 0
        random_rival_hand = 0
        return 'win', deck_on_hand

    if deck_on_hand > 21 > random_rival_hand or \
            (deck_on_hand < random_rival_hand < 21) or \
            (random_rival_hand == 21 and deck_on_hand != 21):

        deck_on_hand = 0
        random_rival_hand = 0
        return 'lose', deck_on_hand

    if (deck_on_hand == 21 and random_rival_hand == 21) or \
            (deck_on_hand > 21 and random_rival_hand > 21):

        deck_on_hand = 0
        random_rival_hand = 0
        return 'draw', deck_on_hand