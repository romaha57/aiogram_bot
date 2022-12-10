from aiogram.dispatcher.filters.state import StatesGroup, State


class TranslateText(StatesGroup):
    """Класс для создания машины состояния при переводе текста"""

    text = State()
