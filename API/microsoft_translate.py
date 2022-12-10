import json
from typing import Dict

import requests
from loguru import logger

from utils.define_translation_params import define_lang, define_querystring_based_on_lang_code


def get_request_to_translate_api(text_for_translate: str) -> (False, str):
	"""Функция для запроса к api Microsoft Translator Text"""

	url = "https://microsoft-translator-text.p.rapidapi.com/translate"
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "71167d0220msh578f46abe7f0198p13dc76jsn741bd8097f76",
		"X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
	}

	lang_code = define_lang(text_for_translate)
	querystring = define_querystring_based_on_lang_code(lang_code=lang_code)

	payload = [{"Text": f"{text_for_translate}"}]

	logger.debug('отправляем post запрос к api microsoft-translator-text')
	response = requests.post(url, json=payload, headers=headers, params=querystring)
	if response.status_code == 200:
		data = json.loads(response.text)
		answer = handle_answer_from_translation_api(text_for_translate=text_for_translate,
													data=data)
		return answer
	else:
		logger.warning('не удалось подключиться к microsoft-translator-text(code != 200)')
		return False


def handle_answer_from_translation_api(text_for_translate: str, data: Dict) -> str:
	"""Функция для преобразования ответа в 1 строку"""

	trans_text = data[0]['translations'][0]['text']

	return f'{text_for_translate}\n------------------------------\n' \
		   f'{trans_text}'