import json
import os
import datetime


def get_all_data() -> list[dict[str, str | int]]:
    '''Функция возвращает данные с JSON файла, где хранятся данные о расписании
    Здесь используется библиотека os для более корректоного указания пути на разных ОС
    Данные возвращаются в виде списка со вложенными словарями
    '''
    with open(os.path.join('data', 'data.json'), 'r', encoding='utf-8') as data:
        return json.load(data)


def get_current_day_data(current_day: str) -> str | list[dict[str, str | int]]:
    '''Функция возвращает данные по дню, который был передан в функцию
    В случае, если в список с результами ничего не было добавлено, возвращается строковое значение
    Функция возвращает список с вложенными словарями
    '''
    data = get_all_data()
    results = []
    for lesson in data:
        if lesson["day_week"] == current_day:
            results.append(lesson)

    if not results:
        return 'Завтра нет пар'
    return results


def search_by_subject(subject_name: str) -> str | list[dict[str, str | int]]:
    '''Функция возвращает данные по дисциплине, которая была передана в функцию
    В случае, когда дисциплина не находится, или пользователь ввёл неверное значение, возвращается строковое значение
    Функция возвращает список с вложенными словарями
    '''
    if type(subject_name) != str:
        return 'Неверный запрос'
    data = get_all_data()
    results = []
    for lesson in data:
        if subject_name.lower() in lesson["discipline"].lower():
            results.append(lesson)
    if not results:
        return 'Такой дисциплины нет в расписании'
    return results


def get_next_day() -> str:
    '''Функция возвращает следующий день на английском языке
    Сначала с помощью библиотеки datetime было получено int значение дня недели по порядку
    Далее с помощью небольшого словаря достаём нашим значением слово и возвращаем его
    '''
    day_order = datetime.datetime.isoweekday(datetime.datetime.now())
    week = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 7
    }
    for k, v in week.items():
        if v - 1 == day_order:
            return k
    return 'sunday'


def translate_day(eng_word: str) -> str:
    '''Функиця возвращает русское слово, переведённое с аннглийского языка, исходя из слова, переданного в функию
    '''
    ru_eng_days = {
        'monday': 'пн',
        'tuesday': 'вт',
        'wednesday': 'ср',
        'thursday': 'чт',
        'friday': 'пт',
        'saturday': 'сб',
        'sunday': 'вс'
    }
    for k, v in ru_eng_days.items():
        if k == eng_word:
            return v
