from phone import WhitePagesPhoneNumber
from location import WhitePagesLocation


class WhitePagesPerson():
    def __init__(self, person_result):
        self.best_name = person_result['best_name']
        self.age_range = person_result['age_range']
        self.gender = person_result['gender']
        self.locations = [WhitePagesLocation(location) for location in person_result['locations']]
        self.names = person_result['names']
        self.phones = [WhitePagesPhoneNumber(phone) for phone in person_result['phones']]
        self.type = person_result['type']
        self.id = person_result['id']


class PersonRequest():
    def __init__(self, name, first_name, middle_name, last_name, suffix, title,
                 street_line_1, street_line_2, city, postal_code, state_code,
                 country_code, use_historical, use_metro):
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.suffix = suffix
        self.title = title
        self.street_line_1 = street_line_1
        self.street_line_2 = street_line_2
        self.city = city
        self.postal_code = postal_code
        self.state_code = state_code
        self.country_code = country_code
        self.use_historical = use_historical
        self.use_metro = use_metro

    def url(self):
        return 'https://proapi.whitepages.com/2.1/person.json?'

    def whitePagesObject(self, query_dict):
        return WhitePagesPerson(query_dict)
