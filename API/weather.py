import json
from typing import Dict

import requests

import config
from utils.transform_weather_params import get_name_location, get_pretty_pressure,\
    get_pretty_sunset, get_pretty_sunrise, transform_visibility_in_pretty,\
    transform_wind_direction_in_pretty


api_key = config.OWM_TOKEN


def get_request_to_weather_api(lat: float, lon: float) -> (False, str):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat=' \
          f'{lat}&lon={lon}&appid={api_key}&lang=ru&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        weather_params = get_weather_parameters(lat, lon, data)
        return weather_params
    else:
        # если не удалось подключиться к сервису
        return False


def get_weather_parameters(lat: float, lon: float, data: Dict) -> str:
    """Из данных полученных от openweathermap получает нужные нам данные для вывода погоды"""

    weather_params = dict()
    weather_params['clouds'] = data.get('weather', {})[0].get('description')
    weather_params['temperature'] = data.get('main', {}).get('temp', {})
    weather_params['temperature_feels'] = data.get('main', {}).get('feels_like')

    # преобразовывает в красивый вид давление
    pressure = data.get('main', {}).get('pressure', {})
    pretty_pressure = get_pretty_pressure(pressure)
    weather_params['pressure'] = pretty_pressure

    weather_params['humidity'] = data.get('main', {}).get('humidity', {})

    # преобразовывает в красивый вид видимость
    visibility = data.get('visibility', {})
    pretty_visibility = transform_visibility_in_pretty(visibility)
    weather_params['visibility'] = pretty_visibility

    weather_params['wind_speed'] = data.get('wind', {}).get('speed', {})

    # преобразовывает в красивый вид направление ветра
    wind_direction = data.get('wind', {}).get('deg', {})
    pretty_wind_direction = transform_wind_direction_in_pretty(wind_direction)
    weather_params['wind_direction'] = pretty_wind_direction

    # преобразовывает в красивый вид восход
    sunrise = data.get('sys', {}).get('sunrise', {})
    pretty_sunrise = get_pretty_sunrise(sunrise)
    weather_params['sunrise'] = pretty_sunrise

    # преобразовывает в красивый вид закат
    sunset = data.get('sys', {}).get('sunset', {})
    pretty_sunset = get_pretty_sunset(sunset)
    weather_params['sunset'] = pretty_sunset

    # получаем строковое название локации
    name_location = get_name_location(lat, lon)
    weather_params['name_location'] = name_location

    answer = do_pretty_weather(weather_params)
    return answer


def do_pretty_weather(weather_params: Dict) -> str:
    """Функция, которая формирует строку для ответа из полученных данных"""

    answer = f'📍 <em>{weather_params["name_location"]}</em>\n\n'\
             f'🌡 Температура: <b>{weather_params["temperature"]} °C</b>' \
             f' (ощущается как <b>{weather_params["temperature_feels"]} °C)</b>\n' \
             f'☁ Облачность: {weather_params["clouds"]}, {weather_params["visibility"]}\n' \
             f'💨 Ветер: <b>{weather_params["wind_direction"]} ' \
             f'{weather_params["wind_speed"]} м/c</b>\n' \
             f'🔹 Давление <b>{weather_params["pressure"]} мм рт.ст.</b>\n' \
             f'💧 Влажность: {weather_params["humidity"]} %\n' \
             f'🌅 Восход : {weather_params["sunrise"]}\n' \
             f'🌇 Закат: {weather_params["sunset"]}'

    return answer
