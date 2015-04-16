try:
    import json
except ImportError:
    import simplejson as json
import urllib
import urllib2

from helper import query
from business import BusinessRequest
from location import LocationRequest
from person import PersonRequest
from phone import PhoneRequest


class WhitePages():
    def __init__(self, api_key):
        self.__api_key = api_key

    def person(self, name=None, first_name=None, middle_name=None, last_name=None, suffix=None, title=None,
               street_line_1=None, street_line_2=None, city=None, postal_code=None, state_code=None,
               country_code=None, use_historical=None, use_metro=None):
        return query(self, PersonRequest(name, first_name, middle_name, last_name, suffix, title, street_line_1,
                                         street_line_2, city, postal_code, state_code, country_code, use_historical,
                                         use_metro))

    def phone(self, phone_number=None, response_type=None):
        return query(self, PhoneRequest(phone_number, response_type))

    def business(self, name=None, street_line_1=None, street_line_2=None, city=None, postal_code=None,
                 state=None, country_code=None):
        return query(self, BusinessRequest(name, street_line_1, street_line_2, city, postal_code, state, country_code))

    def location(self, street_line_1=None, street_line_2=None, city=None, postal_code=None, state_code=None,
                 country_code=None, lat=None, lon=None, radius=None):
        return query(self, LocationRequest(street_line_1, street_line_2, city, postal_code, state_code,
                                           country_code, lat, lon, radius))