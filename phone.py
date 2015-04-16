from business import WhitePagesBusiness
from location import WhitePagesLocation


class PhoneRequest():
    def __init__(self, phone_number, response_type):
        self.phone_number = phone_number
        self.response_type = response_type

    def url(self):
        return 'https://proapi.whitepages.com/2.1/phone.json?'

    def to_dict(self):
        return vars(self)

    def whitePagesObject(self, query_dict):
        return WhitePagesPhoneNumber(query_dict)


class WhitePagesPhoneNumber():
    def __init__(self, phone_result):
        self.phone_number = phone_result['phone_number']
        self.extension = phone_result['extension']
        self.best_location = phone_result['best_location']
        self.associated_locations = [WhitePagesLocation(location) for location in phone_result['associated_locations']]
        self.country_calling_code = phone_result['country_calling_code']
        self.belongs_to = phone_result['belongs_to']
        self.is_valid = phone_result['is_valid']
        self.line_type = phone_result['line_type']
        self.carrier = phone_result['carrier']
        self.do_not_call = phone_result['do_not_call']
        self.id = phone_result['id']
        self.is_prepaid = phone_result['is_prepaid']
        self.reputation = phone_result['reputation']