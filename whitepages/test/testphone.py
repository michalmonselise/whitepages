from unittest2 import TestCase

from whitepages.phone import WhitePagesPhoneNumber


class TestWhitePagesPhoneNumber(TestCase):
    def setUp(self):
        self.basic_input = {
            "results": [
                {
                    "id": {
                        "key": "Phone.4d796fef-a2df-4b08-cfe3-bc7128b6f6bb.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Phone.4d796fef-a2df-4b08-cfe3-bc7128b6f6bb.Durable.json?api_key=LEYVAL",
                        "type": "Phone",
                        "uuid": "4d796fef-a2df-4b08-cfe3-bc7128b6f6bb",
                        "durability": "Durable"
                    },
                    "line_type": "Landline",
                    "belongs_to": [
                        {
                            "id": {
                                "key": "Business.ed5796c8-4e86-480a-b520-7a9f47f03a19.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Business.ed5796c8-4e86-480a-b520-7a9f47f03a19.Durable.json?api_key=LEYVAL",
                                "type": "Business",
                                "uuid": "ed5796c8-4e86-480a-b520-7a9f47f03a19",
                                "durability": "Durable"
                            },
                            "valid_for": None,
                            "name": "Whitepages",
                            "locations": [
                                {
                                    "id": {
                                        "key": "Location.b4bad7f6-4095-4fbf-a997-130984ed94ad.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Location.b4bad7f6-4095-4fbf-a997-130984ed94ad.Durable.json?api_key=LEYVAL",
                                        "type": "Location",
                                        "uuid": "b4bad7f6-4095-4fbf-a997-130984ed94ad",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "type": "Address",
                                    "legal_entities_at": None,
                                    "city": "Palo Alto",
                                    "postal_code": "94306",
                                    "zip4": "2203",
                                    "state_code": "CA",
                                    "country_code": "US",
                                    "address": "411 Acacia Ave, Palo Alto, CA 94306-2203",
                                    "house": "411",
                                    "street_name": "Acacia",
                                    "street_type": "Ave",
                                    "apt_type": None,
                                    "is_receiving_mail": True,
                                    "not_receiving_mail_reason": None,
                                    "usage": None,
                                    "delivery_point": None,
                                    "box_type": None,
                                    "address_type": None,
                                    "lat_long": {
                                        "latitude": 37.4225997924805,
                                        "longitude": -122.138076782227,
                                        "accuracy": "RoofTop"
                                    },
                                    "is_deliverable": True,
                                    "contained_by_locations": None
                                }
                            ],
                            "phones": [
                                {
                                    "id": {
                                        "key": "Phone.4d796fef-a2df-4b08-cfe3-bc7128b6f6bb.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Phone.4d796fef-a2df-4b08-cfe3-bc7128b6f6bb.Durable.json?api_key=LEYVAL",
                                        "type": "Phone",
                                        "uuid": "4d796fef-a2df-4b08-cfe3-bc7128b6f6bb",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "line_type": "Landline",
                                    "belongs_to": None,
                                    "associated_locations": None,
                                    "is_valid": True,
                                    "phone_number": "2069735100",
                                    "country_calling_code": "1",
                                    "extension": None,
                                    "carrier": "tw telecom",
                                    "do_not_call": False,
                                    "reputation": {
                                        "spam_score": 6
                                    },
                                    "is_prepaid": False,
                                    "best_location": None
                                }
                            ]
                        },
                        {
                            "id": {
                                "key": "Business.dfd13b90-b786-4f94-bfd3-b65d5a5cb088.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Business.dfd13b90-b786-4f94-bfd3-b65d5a5cb088.Durable.json?api_key=LEYVAL",
                                "type": "Business",
                                "uuid": "dfd13b90-b786-4f94-bfd3-b65d5a5cb088",
                                "durability": "Durable"
                            },
                            "valid_for": None,
                            "name": "Whitepages",
                            "locations": [
                                {
                                    "id": {
                                        "key": "Location.a3c1ed9b-a709-4b58-a3bf-eb29727f6740.Ephemeral",
                                        "url": None,
                                        "type": "Location",
                                        "uuid": "a3c1ed9b-a709-4b58-a3bf-eb29727f6740",
                                        "durability": "Ephemeral"
                                    },
                                    "contact_type": None,
                                    "type": "Address",
                                    "legal_entities_at": None,
                                    "city": "New York",
                                    "postal_code": "10018",
                                    "zip4": None,
                                    "state_code": "NY",
                                    "country_code": None,
                                    "address": None,
                                    "house": None,
                                    "street_name": None,
                                    "street_type": None,
                                    "apt_type": None,
                                    "is_receiving_mail": None,
                                    "not_receiving_mail_reason": None,
                                    "usage": None,
                                    "delivery_point": None,
                                    "box_type": None,
                                    "address_type": None,
                                    "lat_long": {
                                        "latitude": 40.753017,
                                        "longitude": -73.986237,
                                        "accuracy": None
                                    },
                                    "is_deliverable": None,
                                    "contained_by_locations": None
                                }
                            ],
                            "phones": [
                                {
                                    "id": {
                                        "key": "Phone.4d796fef-a2df-4b08-cfe3-bc7128b6f6bb.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/Phone.4d796fef-a2df-4b08-cfe3-bc7128b6f6bb.Durable.json?api_key=LEYVAL",
                                        "type": "Phone",
                                        "uuid": "4d796fef-a2df-4b08-cfe3-bc7128b6f6bb",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "line_type": "Landline",
                                    "belongs_to": None,
                                    "associated_locations": None,
                                    "is_valid": True,
                                    "phone_number": "2069735100",
                                    "country_calling_code": "1",
                                    "extension": None,
                                    "carrier": "tw telecom",
                                    "do_not_call": False,
                                    "reputation": {
                                        "spam_score": 6
                                    },
                                    "is_prepaid": False,
                                    "best_location": None
                                }
                            ]
                        },
                        {
                            "id": {
                                "key": "Business.545ac847-02be-4f1c-8139-9e7b97b18003.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/Business.545ac847-02be-4f1c-8139-9e7b97b18003.Durable.json?api_key=LEYVAL",
                                "type": "Business",
                                "uuid": "545ac847-02be-4f1c-8139-9e7b97b18003",
                                "durability": "Durable"
                            },
                            "valid_for": None,
                            "name": "Whitepages",
                            "locations": [
                                {
                                    "id": {
                                        "key": "Location.f680d715-f932-4e68-9e64-9871113a6b81.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Location.f680d715-f932-4e68-9e64-9871113a6b81.Durable.json?api_key=LEYVAL",
                                        "type": "Location",
                                        "uuid": "f680d715-f932-4e68-9e64-9871113a6b81",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "type": "Address",
                                    "legal_entities_at": None,
                                    "city": "Seattle",
                                    "postal_code": "98101",
                                    "zip4": "2603",
                                    "state_code": "WA",
                                    "country_code": "US",
                                    "address": "1301 5th Ave, Seattle, WA 98101-2603",
                                    "house": "1301",
                                    "street_name": "5th",
                                    "street_type": "Ave",
                                    "apt_type": None,
                                    "is_receiving_mail": None,
                                    "not_receiving_mail_reason": None,
                                    "usage": None,
                                    "delivery_point": None,
                                    "box_type": None,
                                    "address_type": None,
                                    "lat_long": {
                                        "latitude": 47.608624,
                                        "longitude": -122.334442,
                                        "accuracy": "RoofTop"
                                    },
                                    "is_deliverable": False,
                                    "contained_by_locations": None
                                }
                            ],
                            "phones": [
                                {
                                    "id": {
                                        "key": "Phone.4d796fef-a2df-4b08-cfe3-bc7128b6f6bb.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Phone.4d796fef-a2df-4b08-cfe3-bc7128b6f6bb.Durable.json?api_key=LEYVAL",
                                        "type": "Phone",
                                        "uuid": "4d796fef-a2df-4b08-cfe3-bc7128b6f6bb",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "line_type": "Landline",
                                    "belongs_to": None,
                                    "associated_locations": None,
                                    "is_valid": True,
                                    "phone_number": "2069735100",
                                    "country_calling_code": "1",
                                    "extension": None,
                                    "carrier": "tw telecom",
                                    "do_not_call": False,
                                    "reputation": {
                                        "spam_score": 6
                                    },
                                    "is_prepaid": False,
                                    "best_location": None
                                },
                                {
                                    "id": {
                                        "key": "Phone.345f6fef-a2e1-4b08-cfe3-bc7128b7ba13.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Phone.345f6fef-a2e1-4b08-cfe3-bc7128b7ba13.Durable.json?api_key=LEYVAL",
                                        "type": "Phone",
                                        "uuid": "345f6fef-a2e1-4b08-cfe3-bc7128b7ba13",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "line_type": "Landline",
                                    "belongs_to": None,
                                    "associated_locations": None,
                                    "is_valid": None,
                                    "phone_number": "8003361327",
                                    "country_calling_code": "1",
                                    "extension": None,
                                    "carrier": None,
                                    "do_not_call": None,
                                    "reputation": None,
                                    "is_prepaid": None,
                                    "best_location": None
                                },
                                {
                                    "id": {
                                        "key": "Phone.345f6fef-a2e1-4b08-cfe3-bc7128b7ba13.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Phone.345f6fef-a2e1-4b08-cfe3-bc7128b7ba13.Durable.json?api_key=LEYVAL",
                                        "type": "Phone",
                                        "uuid": "345f6fef-a2e1-4b08-cfe3-bc7128b7ba13",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "line_type": "Landline",
                                    "belongs_to": None,
                                    "associated_locations": None,
                                    "is_valid": None,
                                    "phone_number": "8003361327",
                                    "country_calling_code": "1",
                                    "extension": None,
                                    "carrier": None,
                                    "do_not_call": None,
                                    "reputation": None,
                                    "is_prepaid": None,
                                    "best_location": None
                                }
                            ]
                        }
                    ],
                    "associated_locations": [
                        {
                            "id": {
                                "key": "Location.31d25199-e4db-4b0b-a4e1-c463702f3eb6.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Location.31d25199-e4db-4b0b-a4e1-c463702f3eb6.Durable.json?api_key=LEYVAL",
                                "type": "Location",
                                "uuid": "31d25199-e4db-4b0b-a4e1-c463702f3eb6",
                                "durability": "Durable"
                            },
                            "contact_type": None,
                            "type": "CityPostalCode",
                            "legal_entities_at": None,
                            "city": "Seattle",
                            "postal_code": "98115",
                            "zip4": None,
                            "state_code": "WA",
                            "country_code": "US",
                            "address": "Seattle WA 98115",
                            "house": None,
                            "street_name": None,
                            "street_type": None,
                            "apt_type": None,
                            "is_receiving_mail": None,
                            "not_receiving_mail_reason": None,
                            "usage": None,
                            "delivery_point": None,
                            "box_type": None,
                            "address_type": None,
                            "lat_long": {
                                "latitude": 47.6851,
                                "longitude": -122.2926,
                                "accuracy": "PostalCode"
                            },
                            "is_deliverable": None
                        }
                    ],
                    "is_valid": True,
                    "phone_number": "2069735100",
                    "country_calling_code": "1",
                    "extension": None,
                    "carrier": "tw telecom",
                    "do_not_call": False,
                    "reputation": {
                        "spam_score": 6
                    },
                    "is_prepaid": False,
                    "best_location": {
                        "id": {
                            "key": "Location.31d25199-e4db-4b0b-a4e1-c463702f3eb6.Durable",
                            "url": "https://proapi.whitepages.com/2.1/entity/"
                                   "Location.31d25199-e4db-4b0b-a4e1-c463702f3eb6.Durable.json?api_key=LEYVAL",
                            "type": "Location",
                            "uuid": "31d25199-e4db-4b0b-a4e1-c463702f3eb6",
                            "durability": "Durable"
                        },
                        "type": "CityPostalCode",
                        "legal_entities_at": None,
                        "city": "Seattle",
                        "postal_code": "98115",
                        "zip4": None,
                        "state_code": "WA",
                        "country_code": "US",
                        "address": "Seattle WA 98115",
                        "house": None,
                        "street_name": None,
                        "street_type": None,
                        "apt_type": None,
                        "is_receiving_mail": None,
                        "not_receiving_mail_reason": None,
                        "usage": None,
                        "delivery_point": None,
                        "box_type": None,
                        "address_type": None,
                        "lat_long": {
                            "latitude": 47.6851,
                            "longitude": -122.2926,
                            "accuracy": "PostalCode"
                        },
                        "is_deliverable": None
                    }
                }
            ],
            "messages": []
        }

        def test_phone(self):
            phone_number = [WhitePagesPhoneNumber(phone) for phone in self['results']]
            self.assertEqual(phone_number[0].carrier, 'tw telecom')
            self.assertEqual(phone_number[0].do_not_call, False)



