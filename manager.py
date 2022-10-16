from utils import run_sql, get_common_actors

class Manager:

    def __repr__(self):
        return f"netflix.db sql request manager"


    def title_search(self, user_title):
        """Поиск по названию. Если таких фильмов несколько, выведите самый свежий."""

        sqlite_query = f"""SELECT title, country, release_year, listed_in as genre, description 
        FROM netflix 
        WHERE title LIKE '%{user_title}%' 
        ORDER BY release_year DESC, date_added DESC 
        LIMIT 1"""

        result = run_sql(sqlite_query)
        if result:
            data = dict(result[0])
            return data


    def year_to_year_search(self, year1, year2):
        """Поиск по диапазону лет выпуска. Ограничьте вывод 100 тайтлами."""

        sqlite_query = f"""SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {year1} AND {year2}
        LIMIT 100"""

        data = [dict(row) for row in run_sql(sqlite_query)]
        return data


    def rating_group_search(self, rating_group):
        """Поиск по рейтингу."""

        rating_groups_dict = {
            'children': ('G', 'G'),
            'family': ('G', 'PG', 'PG-13'),
            'adult': ('R', 'NC-17')
        }

        sqlite_query = f"""SELECT title, rating, description
        FROM netflix
        WHERE rating IN  {rating_groups_dict.get(rating_group, (rating_group, 'G'))}
        """

        data = [dict(row) for row in run_sql(sqlite_query)]
        return data


    def genre_search(self, genre):
        """Поиск по жанру. Возвращает 10 самых свежих фильмов."""

        sqlite_query = f"""SELECT title, description
        FROM netflix
        WHERE listed_in LIKE '%{genre}%'
        ORDER BY release_year DESC, date_added DESC
        LIMIT 10"""

        data = [dict(row) for row in run_sql(sqlite_query)]
        return data


    def actors_search(self, name1='Rose McIver', name2='Ben Lamb'):
        """
        Шаг 5 - to do
        Напишите функцию, которая получает в качестве аргумента имена двух актеров, сохраняет всех актеров из колонки cast
        и возвращает список тех, кто играет с ними в паре больше 2 раз.
        Для этого задания не требуется создавать вьюшку
        В качестве теста можно передать: Rose McIver и Ben Lamb, Jack Black и Dustin Hoffman.
        """

        sqlite_query = f"""SELECT `cast`
        FROM netflix
        WHERE `cast` LIKE '%{name1}%' 
        AND `cast` LIKE '%{name2}%' 
        """

        data = [dict(row) for row in run_sql(sqlite_query)]

        common_actors = get_common_actors(data)

        common_actors.remove(name1)
        common_actors.remove(name2)

        return common_actors

    def complex_search(self, type='Movie', release_year=2021, genre='drama'):
        """
        Шаг 6
        Напишите функцию, с помощью которой можно будет передавать **тип** картины (фильм или сериал), **год выпуска** и ее **жанр**
        и получать на выходе список названий картин с их описаниями в JSON.
        Сперва напишите SQL запрос, затем напишите функцию, которая принимала бы `тип, год, жанр`
        Для этого задания не требуется создавать вьюшку
        """

        sqlite_query = f"""SELECT title, description
        FROM netflix
        WHERE type = '{type}'
        AND release_year = '{release_year}'
        AND listed_in LIKE '%{genre}%'
        """

        data = [dict(row) for row in run_sql(sqlite_query)]
        return data


if __name__ == '__main__':

    netflix_dao = Manager()
    print('title_search\n', netflix_dao.title_search('children'))
    print('year_to_year_search\n', netflix_dao.year_to_year_search(2011,2012))
    print('rating_group_search\n', netflix_dao.rating_group_search('children'))
    print('genre_search\n', netflix_dao.genre_search('dramas'))
    print('actors_search\n', netflix_dao.actors_search())
    print('complex_search\n', netflix_dao.complex_search('Movie', 2010, 'drama'))