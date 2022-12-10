from aiogram import types
from aiogram.dispatcher import FSMContext

from states.trans_state import TranslateText
from API.microsoft_translate import get_request_to_translate_api


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
