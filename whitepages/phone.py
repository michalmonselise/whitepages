from warnings import warn

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
        import location
        if self.attr('phone_number', phone_result):
            self.phone_number = phone_result['phone_number']
        else:
            self.phone_number = None
        if self.attr('extension', phone_result):
            self.extension = phone_result['extension']
        else:
            self.extension = None
        if self.attr('best_location', phone_result):
            self.best_location = phone_result['best_location']
        else:
            self.best_location = None
        if self.attr('associated_locations', phone_result):
            self.associated_locations = [location.WhitePagesLocation(l) for l in phone_result['associated_locations']]
        else:
            self.associated_locations = None
        if self.attr('country_call_code', phone_result):
            self.country_calling_code = phone_result['country_calling_code']
        else:
            self.country_calling_code = None
        if self.attr('belongs_to', phone_result):
            self.belongs_to = [belongs_to_object(phone) for phone in phone_result['belongs_to']]
        else:
            self.belongs_to = None
        if self.attr('is_valid', phone_result):
            self.is_valid = phone_result['is_valid']
        else:
            self.is_valid = None
        if self.attr('line_type', phone_result):
            self.line_type = phone_result['line_type']
        else:
            self.line_type = None
        if self.attr('carrier', phone_result):
            self.carrier = phone_result['carrier']
        else:
            self.carrier = None
        if self.attr('do_not_call', phone_result):
            self.do_not_call = phone_result['do_not_call']
        else:
            self.do_not_call = None
        if self.attr('id', phone_result):
            self.id = phone_result['id']
        else:
            self.id = None
        if self.attr('is_prepaid', phone_result):
            self.is_prepaid = phone_result['is_prepaid']
        else:
            self.is_prepaid = None
        if self.attr('reputation', phone_result):
            self.reputation = phone_result['reputation']
        else:
            self.reputation = None

    def attr(self, attribute, result):
        if attribute in result:
            if result[attribute] is not None:
                return True
            return False


def belongs_to_object(belongs_to_result):
    import business
    import person

    if belongs_to_result['id']['type'] == 'Business':
        return business.WhitePagesBusiness(belongs_to_result)
    else:
        if belongs_to_result['id']['type'] == 'Person':
            return person.WhitePagesPerson(belongs_to_result)
        else:
            warning_detail = 'This is not a valid type for belongs_to'
            warn(warning_detail)
            return belongs_to_result
