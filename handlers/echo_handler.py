from aiogram import types

from keyboards.inline_keyboards import create_inline_button_menu


async def echo(message: types.Message) -> None:
    """Отлавливает любые другие сообщения и выводит сообщение с кнопками функций бота"""
    await message.answer('Я вас не понимаю\nВыберите одну из функций',
                         reply_markup=create_inline_button_menu())
