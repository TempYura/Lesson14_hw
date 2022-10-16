from flask import Flask, jsonify

from manager import Manager


netflix_dao = Manager()

app = Flask(__name__)


@app.route('/movie/<title>')
def page_movie_title(title):
    """Поиск по названию. Если таких фильмов несколько, выведите самый свежий."""
    return jsonify(netflix_dao.title_search(title))


@app.route('/movie/<int:year1>/to/<int:year2>')
def page_movie_year_to_year(year1, year2):
    """Поиск по диапазону лет выпуска. Ограничьте вывод 100 тайтлами."""
    return jsonify(netflix_dao.year_to_year_search(year1, year2))


@app.route('/rating/<rating_group>')
def page_rating_rating_group(rating_group):
    """Поиск по рейтингу."""
    return jsonify(netflix_dao.rating_group_search(rating_group))


@app.route('/genre/<genre>')
def page_genre_genre(genre):
    """Поиск по жанру. Возвращает 10 самых свежих фильмов."""
    return jsonify(netflix_dao.genre_search(genre))


if __name__ == '__main__':
    app.run(debug=True)
