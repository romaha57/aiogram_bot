from aiogram import types

from API.card_game_21 import get_first_card, get_more_one_card
from keyboards.card_game_button import create_game_button
from utils.bkackjack_game_params import check_win_or_lose, add_card_in_hands


async def press_start_or_again_card_game(callback: types.CallbackQuery) -> None:
    """Обрабатывает нажатие на кнопку сыграть в карты или на кнопку 'заново' """

    first_card = get_first_card()
    my_hand = add_card_in_hands(first_card)

    await callback.answer()
    await callback.message.answer(f'🔅 Карта: {first_card}\n'
                                  f'Всего очков: <b>{my_hand}</b>',
                                  reply_markup=create_game_button())


async def press_one_more_card(callback: types.CallbackQuery) -> None:
    """Обрабатывает нажатие на кнопку 'еще одна карта' """

    new_card = get_more_one_card()
    my_hand = add_card_in_hands(new_card)

    if new_card is False:
        await callback.message.answer('❌ Произошла ошибка')
    else:
        await callback.answer()
        await callback.message.answer(f'🔅 Карта: {new_card}\n'
                                      f'Всего очков: <b>{my_hand}</b>',
                                      reply_markup=create_game_button())


async def press_open_hand_card_game(callback: types.CallbackQuery) -> None:
    """Обрабатывает нажатие на кнопку 'вскрываемся' """

    result, score = check_win_or_lose()
    if result == 'lose':
        await callback.message.answer('🔴 <b>Вы проиграли</b>')
    elif result == 'draw':
        await callback.message.answer('🔲 <b>Ничья</b>')
    else:
        await callback.message.answer(f'🟢 <b>Вы выиграли</b>')