import json
import requests  # pip install requests
from abc import ABC, abstractmethod
import sqlite3
from database import check_id


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @abstractmethod
    def get_base(self) -> None:
        pass

    @abstractmethod
    def get_coord(self) -> None:
        pass

    @abstractmethod
    def get_coord(self) -> None:
        pass


class Weather(Builder):
    """Geographical coordinates"""

    def __init__(self, latitude, longitude):
        """
        :param latitude:
        :param longitude:
        """
        self.lat = latitude
        self.lon = longitude
        self.url = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid=2a58e0aefff02129c4e7b68e1c970939").text
        self.url_info = json.loads(self.url)

    def get_base(self):
        print(self.url_info['main'])

        database = sqlite3.connect('weather_requests.db')  # Start
        weather_requests_db = database.cursor()
        name = "main"
        weather_requests_db.execute(f"""INSERT INTO main VALUES({check_id(name)},
        {self.url_info['main']['temp']},
        {self.url_info['main']['feels_like']},
        {self.url_info['main']['temp_min']},
        {self.url_info['main']['temp_max']},
        {self.url_info['main']['pressure']},
        {self.url_info['main']['humidity']},
        {self.url_info['main']['sea_level']},
        {self.url_info['main']['grnd_level']})""")
        database.commit()  # End
        database.close()

        return self.url_info['main']

    def get_coord(self):
        print(self.url_info['coord'])

        database = sqlite3.connect('weather_requests.db')  # Start
        weather_requests_db = database.cursor()
        name = "coord"
        weather_requests_db.execute(f"""INSERT INTO coord VALUES({check_id(name)},
        {self.url_info['coord']['lon']},
        {self.url_info['coord']['lat']})""")
        database.commit()  # End
        database.close()

        return self.url_info['coord']

    def get_wind(self):
        print(self.url_info['wind'])

        database = sqlite3.connect('weather_requests.db')  # Start
        weather_requests_db = database.cursor()
        name = "wind"
        weather_requests_db.execute(f"""INSERT INTO wind VALUES({check_id(name)},
        {self.url_info['wind']['speed']},
        {self.url_info['wind']['deg']},
        {self.url_info['wind']['gust']})""")
        database.commit()  # End
        database.close()

        return self.url_info['wind']

# weather = Weather(4, 23)
#
# weather.get_base()
# weather.get_coord()
# weather.get_wind()
