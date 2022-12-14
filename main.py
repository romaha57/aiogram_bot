from aiogram.utils import executor

from handlers.register_all_handlers import register_handlers
from loader_bot import dp
from utils.logging import run_logging

# функция всех хендлеров
register_handlers(dp=dp)

if __name__ == '__main__':
    run_logging()
    executor.start_polling(dispatcher=dp, skip_updates=True)
