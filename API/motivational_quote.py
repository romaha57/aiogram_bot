import requests
from googletrans import Translator
from loguru import logger


def get_request_to_api_motivations() -> (False, str):
    """Функция для гет запроса к api """

    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {
        "key1": "value",
        "key2": "value"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "71167d0220msh578f46abe7f0198p13dc76jsn741bd8097f76",
        "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
    }

    logger.debug('отправляем post запрос к api motivational-quotes1.p.rapidapi.com')
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.text
        trans_quote = translate_quote(data)
        return trans_quote
    else:
        logger.warning('не удалось подключиться к motivational-quotes1.p.rapidapi.com(code != 200)')
        return False


def translate_quote(quote: str) -> str:
    """Переводит цитату"""

    translator = Translator()
    trans_quote = translator.translate(quote, src='en', dest='ru')

    return trans_quote.text

