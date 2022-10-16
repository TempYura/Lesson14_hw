ДЗ https://skyengpublic.notion.site/14-SQL-81d4fb5ceee543f4b55d8484cfeedfe6

Урок 14. SQL

Проект с flask. Вьюшки возваращают данные в json.
Данные в netflix.db.

Для работы с бд используется функция:

def run_sql(sql):
    """Выполняет sql-запрос к netflix.db"""
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        return connection.execute(sql).fetchall()

SQL запросы через sqlite3.

Примечания:
- cast - зарезервированное слово. Чтобы использовать его в качестве названия столбца, необходимо взять в косые кавычки `cast`.
- чтобы вставлять значение переменных в запросе, необходимо использовать f-строки и {имя_переменной}.
- сортировка по нескольким столбцам: ORDER BY release_year DESC, date_added DESC.
- псевдоним для столбца: SELECT title, listed_in as genre
- ограничение по вхождению (%-ноль или больше символов): WHERE title LIKE '%{user_title}%'
- ключевое слово between (включает обе границы):  WHERE release_year BETWEEN {year1} AND {year2}
- ключевое слово in (для проверки наличия в списке) необходимо использовать с кортежем как минимум из 2 элементов.
Для проверки одного значения использовать конструкцию с дублирующимися значениями ('G', 'G')
- ограничение количества выводимых строк: LIMIT 10
- fetchall() - возвращает список словарей
- fetchone() - возвращает словарь
- при использовании row_factory элементы необходимо преобразовать к словарю.