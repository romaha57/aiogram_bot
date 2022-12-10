from aiogram import types

from keyboards.reply_keyboard import all_reply_keyboards
from API.weather import get_request_to_weather_api
from loader_bot import bot


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
