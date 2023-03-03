#!/usr/bin/env python3
import json
from urllib.request import urlopen
import sys


class WeatherError(Exception):
    pass


class City:
    GEO_URL = 'https://geocoding-api.open-meteo.com/v1/search?name={city}'

    def __init__(self, name):
        self.name = name
        self.latitude = None
        self.longitude = None

    def get_coords(self):

        if self.latitude is not None and self.longitude is not None:
            return
        url = self.GEO_URL.format(city=self.name)
        data = self._make_request(url)
        data = data['results']
        self.name = data[0]['name']
        self.latitude = data[0]['latitude']
        self.longitude = data[0]['longitude']

    @staticmethod
    def _make_request(url):
        response = urlopen(url)
        data = response.read()
        data = data.decode('utf-8')
        res = json.loads(data)

        if 'error' in res:
            raise WeatherError(res['error']['message'])
        return res


class Weather:
    ENDPOINT_URL = 'https://api.open-meteo.com/v1/forecast?{params}'

    def __init__(self, city):
        self.city = city
        self.temperature = None

    def request_curtemp(self):

        if self.temperature is not None:
            return
        url = self._req_url(latitude=self.city.latitude,
                            longitude=self.city.longitude,
                            current_weather='true')
        resp = self._make_request(url)

        try:
            current = resp['current_weather']
            self.temperature = float(current['temperature'])
        except (KeyError, TypeError):
            raise WeatherError('Unable to parse weather data')

    def _req_url(self, **kwargs):
        params = '&'.join([f'{k}={v}' for k, v in kwargs.items()])
        return self.ENDPOINT_URL.format(params=params)

    @staticmethod
    def _make_request(url):
        response = urlopen(url)
        data = response.read()
        data = data.decode('utf-8')
        res = json.loads(data)

        if 'error' in res:
            raise WeatherError(res['error']['message'])
        return res


if __name__ == '__main__':
    USAGE = 'USAGE: {prog} CITY\nGet current temperature.'
    prog, *args = sys.argv

    if len(args) != 1:
        exit(USAGE.format(prog=prog))

    city_name = args[0]
    city = City(city_name)
    city.get_coords()

    weather = Weather(city)
    weather.request_curtemp()

    _deg = '\u00b0'
    print(f'Currently in {city.name} is {weather.temperature} {_deg}C')
