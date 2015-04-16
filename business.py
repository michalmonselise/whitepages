from location import WhitePagesLocation
from phone import WhitePagesPhoneNumber


class BusinessRequest():
    def __init__(self, name, street_line_1, street_line_2, city, postal_code,
                 state, country_code):
        self.name = name
        self.street_line_1 = street_line_1
        self.street_line_2 = street_line_2
        self.city = city
        self.postal_code = postal_code
        self.state = state
        self.country_code = country_code

    def url(self):
        return 'https://proapi.whitepages.com/2.1/business.json?'

    def to_dict(self):
        return vars(self)

    def whitePagesObject(self, query_dict):
        return WhitePagesBusiness(query_dict)


class WhitePagesBusiness():
    def __init__(self, business_result):
        self.id = business_result['id']
        self.name = business_result['name']
        self.locations = [WhitePagesLocation(location) for location in business_result['locations']]
        self.phones = [WhitePagesLocation(phone) for phone in business_result['phones']]

