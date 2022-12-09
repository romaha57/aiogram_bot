from aiogram.utils import executor

from handlers import register_handlers
from loader_bot import dp

# функция всех хендлеров
register_handlers(dp=dp)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
