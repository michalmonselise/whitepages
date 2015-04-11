try:
    import json
except ImportError:
    import simplejson as json
import urllib
import urllib2
import warnings


class WhitePagesError(Exception):
    pass


class WhitePages():
    def __init__(self, api_key):
        self.__api_key = api_key

    def combine_query_with_key(self, keys, query):
        new_keys = ['api_key'] + keys
        new_query = [self.__api_key] + query
        return new_keys, new_query

def extract_url(function_type):
    url_dict = {'person': 'https://proapi.whitepages.com/2.1/person.json?',
                'phone': 'https://proapi.whitepages.com/2.1/phone.json?',
                'business': 'https://proapi.whitepages.com/2.1/business.json?'}
    return url_dict[function_type]


class WhitePagesPerson():
    def __init__(self, best_name, age_range, gender, locations, names, phones, type, id):
        self.best_name = person_result['best_name']
        self.age_range = person_result['age_range']
        self.gender = person_result['gender']
        self.locations = person_result['locations']
        self.names = person_result['names']
        self.phones = person_result['phones']
        self.type = person_result['type']
        self.id = person_result['id']

class Person():
    def __init__(self, name=None, first_name=None, middle_name=None, last_name=None, suffix=None, title=None,
                 street_line_1=None, street_line_2=None, city=None, postal_code=None, state_code=None,
                 country_code=None, use_historical=None, use_metro=None):
        self.name = name
        self.first_name = first_name

    @staticmethod
    def url():
        return 'https://proapi.whitepages.com/2.1/person.json?'

    def whitePagesObject(self):
        return WhitePagesPerson()

def person(name=None, first_name=None, middle_name=None, last_name=None, suffix=None, title=None,
           street_line_1=None, street_line_2=None, city=None, postal_code=None, state_code=None,
           country_code=None, use_historical=None, use_metro=None):
    person_dict = {'name': name, 'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name,
                   'suffix': suffix, 'title': title, 'street_line_1': street_line_1, 'street_line_2': street_line_2,
                   'city': city, 'postal_code': postal_code, 'state_code': state_code, 'country_code': country_code,
                   'use_historical': use_historical, 'use_metro': use_metro}
    url = extract_url('person')
    url_query = url + url_encoder(person_dict)
    person_json = return_json(url_query)
    validate_url(person_json)
    person_json_result = person_json['results']
    person_result = []
    for pr in person_json_result:
        person_result.append(WhitePagesPerson(pr))
    return person_result


class WhitePagesPhoneNumber():
    def __init__(self, phone_result):
        self.phone_number = phone_result['phone_number']
        self.extension = phone_result['extension']
        self.best_location = phone_result['best_location']
        self.associated_locations = phone_result['associated_locations']
        self.country_calling_code = phone_result['country_code']
        self.belongs_to = phone_result['belongs_to']
        self.is_valid = phone_result['is_valid']
        self.line_type = phone_result['line_type']
        self.carrier = phone_result['carrier']
        self.do_not_call = phone_result['do_not_call']
        self.id = phone_result['id']
        self.is_prepaid = phone_result['is_prepaid']
        self.reputation = phone_result['reputation']


def phone(phone_number=None, response_type=None):
    phone_dict = {'phone_number': phone_number, 'response_type': response_type}
    phone_result = query(phone_dict, 'phone')
    return phone_result


class WhitePagesBusiness():
    def __init__(self, business_result):
        self.id = business_result['id']
        self.name = business_result['name']
        self.locations = business_result['locations']
        self.phones = business_result['phones']


def business(name=None, street_line_1=None, street_line_2=None, city=None, postal_code=None,
             state=None, country_code=None):
    business_dict = {'name': name, 'street_line_1': street_line_1, 'street_line_2': street_line_2,
                     'city': city, 'postal_code': postal_code, 'state': state, 'country_code': country_code}
    business_result = query(business_dict, 'business')
    return business_result


def query(input_dict, function_type):
    url = extract_url(function_type)
    input_dict = remove_blank_fields(input_dict)
    if dictIsEmpty(input_dict):
        error_detail = 'You have not entered any valid arguments'
        raise WhitePagesError, error_detail

    url_query = url + url_encoder(input_dict)
    json_blob = return_json(url_query)
    validate_url(json_blob)
    json_result = json_blob['results']
    result = []
    for pr in json_result:
        result.append(WhitePagesBusiness(pr))
    return result

def url_encoder(params):
    encoded_params = urllib.urlencode(params)
    return encoded_params


def return_json(url):
    result_dict = json.load(urllib.urlopen(url))
    return result_dict


def validate_url(result):
    if 'error' in result.keys():
        error_detail = result['error']
        raise WhitePagesError, error_detail


def dictIsEmpty(input_dict):
    return bool(input_dict)


def remove_blank_fields(input_dict):
    return dict((k, v) for k, v in input_dict.iteritems() if v is not None)


