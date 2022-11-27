import unittest
from random import randint
from main import Weather


class TestEmployee(unittest.TestCase):

    def test_all(self):
        for i in range(10):
            print("=" + "-" * 80 + "=")
            weather = Weather(randint(0, 20), randint(0, 20))
            weather.get_base()
            weather.get_coord()
            weather.get_wind()


if __name__ == '__main__':
    unittest.main()
