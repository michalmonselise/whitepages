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
        if self.attr('id', location_result):
            self.id = location_result['id']
        else:
            self.id = None
        if self.attr('type', location_result):
            self.type = location_result['type']
        else:
            self.type = None
        if self.attr('legal_entities_at', location_result):
            self.legal_entities_at = location_result['legal_entities_at']
        else:
            self.legal_entities_at = None
        if self.attr('city', location_result):
            self.city = location_result['city']
        else:
            self.city = None
        if self.attr('postal_code', location_result):
            self.postal_code = location_result['postal_code']
        else:
            self.postal_code = None
        if self.attr('zip4', location_result):
            self.zip4 = location_result['zip4']
        else:
            self.zip4 = None
        if self.attr('state_code', location_result):
            self.state_code = location_result['state_code']
        else:
            self.state_code = None
        if self.attr('country_code', location_result):
            self.country_code = location_result['country_code']
        else:
            self.country_code = None
        if self.attr('address', location_result):
            self.address = location_result['address']
        else:
            self.address = None
        if self.attr('house', location_result):
            self.house = location_result['house']
        else:
            self.house = None
        if self.attr('street_name', location_result):
            self.street_name = location_result['street_name']
        else:
            self.street_name = None
        if self.attr('street_type', location_result):
            self.street_type = location_result['street_type']
        else:
            self.street_type = None
        if self.attr('pre_dir', location_result):
            self.pre_dir = location_result['pre_dir']
        else:
            self.pre_dir = None
        if self.attr('post_dir', location_result):
            self.post_dir = location_result['post_dir']
        else:
            self.post_dir = None
        if self.attr('apt_number', location_result):
            self.apt_number = location_result['apt_number']
        else:
            self.apt_number = None
        if self.attr('apt_type', location_result):
            self.apt_type = location_result['apt_type']
        else:
            self.apt_type = None
        if self.attr('box_number', location_result):
            self.box_number = location_result['box_number']
        else:
            self.box_number = None
        if self.attr('standard_address_line1', location_result):
            self.standard_address_line1 = location_result['standard_address_line1']
        else:
            self.standard_address_line1 = None
        if self.attr('standard_address_line2', location_result):
            self.standard_address_line2 = location_result['standard_address_line2']
        else:
            self.standard_address_line2 = None
        if self.attr('standard_address_location', location_result):
            self.standard_address_location = location_result['standard_address_location']
        else:
            self.standard_address_location = None
        if self.attr('is_receiving_mail', location_result):
            self.is_receiving_mail = location_result['is_receiving_mail']
        else:
            self.is_receiving_mail = None
        if self.attr('not_receiving_mail_reason', location_result):
            self.not_receiving_mail_reason = location_result['not_receiving_mail_reason']
        else:
            self.not_receiving_mail_reason = None
        if self.attr('usage', location_result):
            self.usage = location_result['usage']
        else:
            self.usage = None
        if self.attr('delivery_point', location_result):
            self.delivery_point = location_result['delivery_point']
        else:
            self.delivery_point = None
        if self.attr('box_type', location_result):
            self.box_type = location_result['box_type']
        else:
            self.box_type = None
        if self.attr('address_type', location_result):
            self.address_type = location_result['address_type']
        else:
            self.address_type = None
        if self.attr('lat_long', location_result):
            self.lat_long = location_result['lat_long']
        else:
            self.lat_long = None
        if self.attr('is_deliverable', location_result):
            self.is_deliverable = location_result['is_deliverable']
        else:
            self.is_deliverable = None


    def attr(self, attribute, result):
        if attribute in result:
            if result[attribute] is not None:
                return True
            return False
