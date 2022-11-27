import sqlite3


def check_id(name):
    name = str(name)
    output_main_id = 0

    database = sqlite3.connect('weather_requests.db')  # Start
    weather_requests_db = database.cursor()

    weather_requests_db.execute(f"SELECT MAX(route_id) FROM {name};")
    output_main_id = weather_requests_db.fetchone()[0]

    if output_main_id == None:  # Перевірка на те чи є рядки в таблиці
        output_main_id = 1
    else:
        output_main_id += 1

    database.commit()  # End
    database.close()

    return output_main_id
