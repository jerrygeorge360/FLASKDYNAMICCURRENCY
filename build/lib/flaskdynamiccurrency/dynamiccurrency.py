from flask import request, current_app
from flaskdynamiccurrency.reader import CordReader, map_iso
from flaskdynamiccurrency.api_services import *

coord = CordReader()


class DynamicCurrency:

    def __init__(self, app=None):
        self.app_instance = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app_instance = app
        self.app_instance.config.setdefault('geolocation', {'longitude': 0.0, 'latitude': 0.0})
        self.app_instance.extensions['GEOCONVEXT'] = self
        self.routing_system()
        if hasattr(app, 'add_template_global'):
            app.add_template_global(self.api_services, 'api_services')
        else:
            app.jinja_env.globals['api_services'] = self.api_services

    def routing_system(self):
        @self.app_instance.post('/geo_route')
        def get_location():
            data = request.get_json()
            current_app.config['geolocation']['longitude'] = data[0]
            current_app.config['geolocation']['latitude'] = data[1]
            coord.init_app(current_app.config['geolocation']['longitude'],
                           current_app.config['geolocation']['latitude'], "flaskdynamiccurrency/country-by-geo-cordinations.json")
            location_currency = self.map_countries_symbols(country_name=coord.logic())
            current_app.config['geolocation']['location_currency'] = location_currency

            # result = self.api_services(current_app, base_currency=base_currency, amount=amount)

            return 'ok'

    def api_services(self, base_currency='USD', amount='100'):
        try:
            location_currency = self.app_instance.config['geolocation']['location_currency']
            self.app_instance.extensions.get('GEOCONVEXT')
            converted_currency = ninja_currency(base_currency=base_currency, location_currency=location_currency,
                                                amount=amount)
            print(self.app_instance.config)
            return converted_currency


        except:
            print('Problem occured')

        finally:
            pass

    @staticmethod
    def map_countries_symbols(country_name=None):
        return map_iso(path='flaskdynamiccurrency/country _ISO 4217_name.json', country_name=country_name)
