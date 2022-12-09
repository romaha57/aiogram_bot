from aiogram.dispatcher.filters.state import State, StatesGroup


class TranslateText(StatesGroup):
    text = State()
