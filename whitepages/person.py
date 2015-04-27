class WhitePagesPerson():
    def __init__(self, person_result):
        import phone
        import location
        if self.attr('best_name', person_result):
            self.best_name = person_result['best_name']
        else:
            self.best_name = None
        if self.attr('age_range', person_result):
            self.age_range = person_result['age_range']
        else:
            self.age_range = None
        if self.attr('gender', person_result):
            self.gender = person_result['gender']
        else:
            self.gender = None
        if self.attr('locations', person_result):
            self.locations = [location.WhitePagesLocation(l) for l in person_result['locations']]
        else:
            self.locations = None
        if self.attr('names', person_result):
            self.names = person_result['names']
        else:
            self.names = None
        if self.attr('phones', person_result):
            self.phones = [phone.WhitePagesPhoneNumber(p) for p in person_result['phones']]
        else:
            self.phones = None
        if self.attr('type', person_result):
            self.type = person_result['type']
        else:
            self.type = None
        if self.attr('id', person_result):
            self.id = person_result['id']
        else:
            self.id = None

    def attr(self, attribute, result):
        if attribute in result:
            if result[attribute] is not None:
                return True
            return False


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

    def to_dict(self):
        return vars(self)

    def whitePagesObject(self, query_dict):
        return WhitePagesPerson(query_dict)
