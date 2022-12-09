from typing import Dict

import langdetect
from langdetect import DetectorFactory


def define_lang(text: str) -> str:
    """Функция для определения языка ввода и получения его кода"""

    DetectorFactory.seed = 0
    lang_code = langdetect.detect(text)
    return lang_code


def define_querystring_based_on_lang_code(lang_code: str) -> Dict:
    """Функция для определения параметров post запроса исходя из языка,
    на котором ввел пользователь текст"""

    if lang_code == 'en':
        # для перевода с английского на русский
        querystring = {"to[0]": "ru", "api-version": " 3.0", "from": "en",
                       "profanityAction": "NoAction", "textType": "plain"}
    elif lang_code == 'ru':
        # для перевода с русского на английский
        querystring = {"to[0]": "en", "api-version": " 3.0", "from": "ru",
                       "profanityAction": "NoAction", "textType": "plain"}
    elif lang_code in ('mk','uk'):
        # часто библиотека langdetect путает ru с mk,
        # поэтому заменяем все mk на ru
        querystring = {"to[0]": "en", "api-version": " 3.0", "from": "ru",
                       "profanityAction": "NoAction", "textType": "plain"}
    else:
        # перевод с определенного библиотекой языка на русский
        querystring = {"to[0]": "ru", "api-version": " 3.0", "from": f"{lang_code}",
                       "profanityAction": "NoAction", "textType": "plain"}

    return querystring
