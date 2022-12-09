import os

from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не найдены')
elif load_dotenv():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    OWM_TOKEN = os.getenv('OWM_TOKEN')
    RAPIDAPI_TOKEN = os.getenv('RAPIDAPI_TOKEN')
else:
    exit('Переменные окружения не верные')
