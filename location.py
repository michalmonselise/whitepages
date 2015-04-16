class LocationRequest():
    def __init__(self, street_line_1, street_line_2, city, postal_code, state_code,
                 country_code, lat, lon, radius):
        self.street_line_1 = street_line_1
        self.street_line_2 = street_line_2
        self.city = city
        self.postal_code = postal_code
        self.state_code = state_code
        self.country_code = country_code
        self.lat = lat
        self.lon = lon
        self.radius = radius

    def url(self):
        return 'https://proapi.whitepages.com/2.1/location.json?'

    def to_dict(self):
        return vars(self)

    def whitePagesObject(self, query_dict):
        return WhitePagesLocation(query_dict)


class WhitePagesLocation():
    def __init__(self, location_result):
        self.id = location_result['id']
        self.type = location_result['type']
        self.legal_entities_at = location_result['legal_entities_at']
        self.city = location_result['city']
        self.postal_code = location_result['postal_code']
        self.zip4 = location_result['zip4']
        self.state_code = location_result['state_code']
        self.country_code = location_result['country_code']
        self.address = location_result['address']
        self.house = location_result['house']
        self.street_name = location_result['street_name']
        self.street_type = location_result['street_type']
        self.pre_dir = location_result['pre_dir']
        self.post_dir = location_result['post_dir']
        self.apt_number = location_result['apt_number']
        self.apt_type = location_result['apt_type']
        self.box_number = location_result['box_number']
        self.standard_address_line1 = location_result['standard_address_line1']
        self.standard_address_line2 = location_result['standard_address_line2']
        self.standard_address_location = location_result['standard_address_location']
        self.is_receiving_mail = location_result['is_receiving_mail']
        self.not_receiving_mail_reason = location_result['not_receiving_mail_reason']
        self.usage = location_result['usage']
        self.delivery_point = location_result['delivery_point']
        self.box_type = location_result['box_type']
        self.address_type = location_result['address_type']
        self.lat_long = location_result['lat_long']
        self.is_deliverable = location_result['is_deliverable']



