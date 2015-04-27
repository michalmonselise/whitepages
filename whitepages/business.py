class WhitePagesBusiness():
    def __init__(self, business_result):
        import phone
        import location
        if self.attr('id', business_result):
            self.id = business_result['id']
        else:
            self.id = None
        if self.attr('name', business_result):
            self.name = business_result['name']
        else:
            self.name = None
        if self.attr('locations', business_result):
            self.locations = [location.WhitePagesLocation(l) for l in business_result['locations']]
        else:
            self.locations = None
        if self.attr('phones',business_result):
            self.phones = [phone.WhitePagesPhoneNumber(p) for p in business_result['phones']]
        else:
            self.phone = None

    def attr(self, attribute, result):
        if attribute in result:
            if result[attribute] is not None:
                return True
            return False

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


