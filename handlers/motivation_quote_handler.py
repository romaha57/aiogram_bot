from aiogram import types

from API.motivational_quote import get_request_to_api_motivations


async def press_motivation_button(callback: types.CallbackQuery) -> None:
    """Обрабатывает нажатие на кнопку мотивации"""

    answer = get_request_to_api_motivations()
    await callback.answer()
    if answer:
        await callback.message.answer(answer)
    else:
        await callback.message.answer('❌ Сервер временно недоступен\nПопробуйте немного позже')
