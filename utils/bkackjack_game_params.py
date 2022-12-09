suits_card = {'S': '♠', 'D': '♦', 'C': '♣', 'H': '♥'}
values_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               '0': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
high_card = {'J': 'валет', 'Q': 'королева', 'K': 'король', 'A': 'туз'}


deck_on_hand = 0


def pretty_card_suit_and_value(card: str) -> str:
    """Преобразует значение карты в красивый вид"""

    value = card[0]
    suit = card[1]
    pretty_value = values_card[value] if value not in high_card \
        else f'{high_card[value]} ({str(values_card[value])})'

    pretty_suit = suits_card[suit]

    return f'{pretty_value} {pretty_suit}'


def check_win(card):
    card_params = card.split()
    if len(card_params) == 2:
        value = int(card_params[0])
    else:
        value = int(card_params[1].strip('()'))
    global deck_on_hand
    deck_on_hand += value
    print(deck_on_hand)
    if deck_on_hand == 21:
        deck_on_hand = 0
        return 'win'
    elif deck_on_hand > 21:
        deck_on_hand = 0
        return 'lose'


