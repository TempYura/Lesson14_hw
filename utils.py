import sqlite3

def run_sql(sql):
    """Выполняет sql-запрос к netflix.db"""
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        return connection.execute(sql).fetchall()


def get_common_actors(data, n=3):
    """
    Подсчитывает количество упоминаний актеров в списке фильмов
    и возвращает список актеров, у которых количество упоминаний больше или равно n
    """

    # Собираем словарь вида {имя: кол-во упоминаний}
    names_count_dict = {}

    for film in data:
        film_actors_list = film['cast'].split(', ')
        for name in film_actors_list:
            names_count_dict[name] = names_count_dict.get(name, 0) + 1

    # Формируем список имен, у которых кол-во упоминаний больше или равно n
    common_actors_list = [name for name, value in names_count_dict.items() if value >= n]

    return common_actors_list
