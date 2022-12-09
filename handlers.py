from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from keyboards.inline_keyboards import create_inline_button_menu
from keyboards.reply_keyboard import all_reply_keyboards
from keyboards.card_game_button import create_game_button
from API.weather import get_request_to_weather_api
from API.microsoft_translate import get_request_to_translate_api
from API.motivational_quote import get_request_to_api_motivations
from API.card_game_21 import get_first_card, get_more_one_card
from loader_bot import bot
from FMS import TranslateText
from utils.bkackjack_game_params import add_card_in_hands, check_win_or_lose


async def start_help(message: types.Message) -> None:
    """Функция, для отлова команды start и help"""

    await message.answer('🤖 Данный бот имеет множество полезных функций\n'
                         'Выберите одну из них', reply_markup=create_inline_button_menu())


async def press_weather_button(callback: types.CallbackQuery) -> None:
    """Обработчик нажатия на кнопку погоды"""

    await callback.message.answer(
        '📍 Для точного прогноза погоды в вашем районе отправьте свою геопозицию по кнопки ниже',
        reply_markup=all_reply_keyboards)
    await callback.answer()


async def get_weather_from_api(message: types.Message) -> None:
    """Обрабатывает геопозицию и отправляет координаты
    для получения погоды из openweathermap API"""

    latitude = message.location['latitude']
    longitude = message.location['longitude']
    response_weather = get_request_to_weather_api(lat=latitude, lon=longitude)
    if response_weather:

        # отправляем погоду
        await bot.send_message(message.from_user.id, response_weather)

    else:
        # если не удастся подключить к API
        await bot.send_message(message.chat.id, '❌ Сервер погоды временно недоступен\n'
                                                'Попробуйте немного позже')


async def press_translation_button(callback: types.CallbackQuery) -> None:
    """Обрабатывает нажатие на кнопку перевода текста"""

    await callback.message.answer('Введите слово для перевода')

    # устанавливаем машину состояний на слово для перевода
    await TranslateText.text.set()
    await callback.answer()


async def get_translation_text(message: types.Message, state: FSMContext) -> None:
    """Ловим слова для перевода и отправляем пользователю"""

    async with state.proxy() as data:
        data['text'] = message.text

    answer = get_request_to_translate_api(data["text"])

    # завершаем отлов состояний
    await state.finish()

    if answer:
        await message.answer(answer)
    else:
        await message.answer('❌ Сервер перевода текста временно недоступен\n'
                             'Попробуйте немного позже')


async def press_motivation_button(callback: types.CallbackQuery) -> None:
    """Обрабатывает нажатие на кнопку мотивации"""

    answer = get_request_to_api_motivations()
    await callback.answer()
    if answer:
        await callback.message.answer(answer)
    else:
        await callback.message.answer('❌ Сервер временно недоступен\nПопробуйте немного позже')


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


async def echo(message: types.Message) -> None:
    """Отлавливает любые другие сообщения и выводит сообщение с кнопками функций бота"""
    await message.answer('Я вас не понимаю\nВыберите одну из функций',
                         reply_markup=create_inline_button_menu())


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
