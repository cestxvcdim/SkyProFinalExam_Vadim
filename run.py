import logging
from flask import Flask, request, render_template, jsonify
from utils import *

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False
app.static_folder = app.root_path + "/static/"

logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    encoding='utf-8',
    format="%(asctime)s : %(levelname)s : %(message)s"
)


@app.route('/')
def main_page():
    data = get_all_data()
    day = get_next_day()
    logging.info('Нахожусь на главной странице')
    return render_template('index.html', data=data, day=day)


@app.route('/weekdays/<weekday>')
def next_day_page(weekday):
    day_query = translate_day(weekday)
    data = get_current_day_data(day_query)
    weekday = weekday.title()
    logging.info(f'Нахожусь на странице с расписанием на {day_query}')
    return render_template('weekday.html', data=data, weekday=weekday)


@app.route('/search')
def search_page():
    search_query = request.args.get('s')
    data = search_by_subject(search_query)
    day = get_next_day()
    subject_name = search_query.title()
    if type(data) == str:
        return f'<h1>{data}</h1>'
    logging.info(f'Обрабатываю результаты по запросу {search_query}')
    return render_template('search.html', data=data, day=day, subject_name=subject_name)


@app.route('/api/data')
def api_data():
    data = get_all_data()
    logging.info('Получены все данные в формате JSON')
    return jsonify(data)


@app.route('/api/data/<weekday>')
def api_data_weekday(weekday):
    day = translate_day(weekday)
    data = get_current_day_data(day)
    logging.info(f'Получены все данные в формате JSON по дню {day}')
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Страница не найдена</h1>'


@app.errorhandler(500)
def page_not_found(e):
    return '<h1>Ошибка на стороне сервера</h1>'


if __name__ == '__main__':
    app.run()
