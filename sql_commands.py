import sqlite3

database = sqlite3.connect('weather_requests.db')  # Start
weather_requests_db = database.cursor()

"""
Створоення і очищення таблиці з назвою main
"""
truthfulness_01 = False
"""
Створоення і очищення таблиці з назвою coord
"""
truthfulness_02 = False
"""
Створоення і очищення таблиці з назвою wind
"""
truthfulness_03 = False

if truthfulness_01:
    weather_requests_db.execute("DROP TABLE main")

    weather_requests_db.execute("""CREATE TABLE main (
    route_id integer,
    temp real,
    feels_like real,
    temp_min real,
    temp_max real,
    pressure real,
    humidity real,
    sea_level real,
    grnd_level real
    )""")

if truthfulness_02:
    weather_requests_db.execute("DROP TABLE coord")

    weather_requests_db.execute("""CREATE TABLE coord (
    route_id integer,
    lon real,
    lat real
    )""")

if truthfulness_03:
    weather_requests_db.execute("DROP TABLE wind")

    weather_requests_db.execute("""CREATE TABLE wind (
    route_id integer,
    speed real,
    deg real,
    gust real
    )""")

database.commit()  # End
database.close()
