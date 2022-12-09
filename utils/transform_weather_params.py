import datetime
import time

from geopy.geocoders import Nominatim


user_agent_for_geopy = 'Mozilla Firefox 36 (Win 8.1 x64): Mozilla/5.0 ' \
                       '(Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0.'


def get_name_location(lat: float, lon: float) -> str:
    """Функция для определения нашей текущий геопозиции(в читабельном виде)
    с помощью координат"""

    geolocator = Nominatim(user_agent=user_agent_for_geopy)
    location = geolocator.reverse(f"{lat}, {lon}")

    return location.address


def transform_visibility_in_pretty(visibility: int) -> str:
    """Переводит значение visibility(видимость) в человеко-понятный вид"""
    if visibility >= 9000:
        return 'отличная видимость'
    elif visibility >= 1000:
        return 'хорошая видимость'
    elif visibility >= 500:
        return 'плохая видимость'
    elif visibility >= 0:
        return 'очень плохая видимость'


def transform_wind_direction_in_pretty(wind_direction: float) -> str:
    """Переводит градус направления ветра в буквенное выражение"""

    # словарь для перевода из градусов в буквы
    transform_wind_direction_dict = {
        'СЗ': range(22, 68),
        'З': range(68, 113),
        'ЮЗ': range(113, 157),
        'Ю': range(157, 203),
        'ЮВ': range(203, 247),
        'В': range(247, 293),
        'СВ': range(293, 340)
    }
    for key, value in transform_wind_direction_dict.items():
        if wind_direction in value:
            return key
    else:
        return 'С'


def get_pretty_pressure(pressure: float) -> int:
    """Переводит давление из гПа в мм рт.ст."""

    return int(pressure * 0.750063755419211)


def get_pretty_sunrise(sunrise: datetime.datetime.timestamp) -> str:
    """Преобразовывает timestamp восхода в строковое значение времени"""

    sunrise_hours = time.ctime(sunrise).split()[3]
    return sunrise_hours[:-3]


def get_pretty_sunset(sunset: datetime.datetime.timestamp) -> str:
    """Преобразовывает timestamp заката в строковое значение времени"""
    sunset_hours = time.ctime(sunset).split()[3]
    return sunset_hours[:-3]