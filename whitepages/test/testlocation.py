from unittest2 import TestCase

from whitepages.location import WhitePagesLocation


class TestWhitePagesLocation(TestCase):
    def setUp(self):
        self.basic_input = {
            "results": [
                {
                    "id": {
                        "key": "Location.efe46385-b057-40c3-8b67-f5a5278e0710.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Location.efe46385-b057-40c3-8b67-f5a5278e0710.Durable.json?api_key=KEYVAL",
                        "type": "Location",
                        "uuid": "efe46385-b057-40c3-8b67-f5a5278e0710",
                        "durability": "Durable"
                    },
                    "type": "Address",
                    "legal_entities_at": [
                        {
                            "id": {
                                "key": "Person.cf0993f8-ea1a-4fe6-9bae-cbca443a09f2.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Person.cf0993f8-ea1a-4fe6-9bae-cbca443a09f2.Durable.json?api_key=KEYVAL",
                                "type": "Person",
                                "uuid": "cf0993f8-ea1a-4fe6-9bae-cbca443a09f2",
                                "durability": "Durable"
                            },
                            "valid_for": {
                                "start": {
                                    "year": 2011,
                                    "month": 6,
                                    "day": 28
                                },
                                "stop": None
                            },
                            "type": "Full",
                            "names": [
                                {
                                    "salutation": None,
                                    "first_name": "Roey",
                                    "middle_name": "F",
                                    "last_name": "Horns",
                                    "suffix": None,
                                    "valid_for": None
                                }
                            ],
                            "age_range": {
                                "start": 45,
                                "end": 49
                            },
                            "gender": None,
                            "locations": [
                                {
                                    "id": {
                                        "key": "Location.efe46385-b057-40c3-8b67-f5a5278e0710.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/"
                                               "entity/Location.efe46385-b057-40c3-8b67-f5a5278e0710.Durable.json?"
                                               "api_key=KEYVAL",
                                        "type": "Location",
                                        "uuid": "efe46385-b057-40c3-8b67-f5a5278e0710",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Home",
                                    "type": "Address",
                                    "legal_entities_at": None,
                                    "city": "Seattle",
                                    "postal_code": "98119",
                                    "zip4": "2043",
                                    "state_code": "WA",
                                    "country_code": "US",
                                    "address": "413 W Howe St, Seattle WA 98119-2043",
                                    "house": "413",
                                    "street_name": "Howe",
                                    "street_type": "St",
                                    "apt_type": None,
                                    "is_receiving_mail": True,
                                    "not_receiving_mail_reason": None,
                                    "usage": "Residential",
                                    "delivery_point": "SingleUnit",
                                    "box_type": None,
                                    "address_type": "Street",
                                    "lat_long": {
                                        "latitude": 47.636105,
                                        "longitude": -122.362549,
                                        "accuracy": "RoofTop"
                                    },
                                    "is_deliverable": True,
                                    "contained_by_locations": None
                                }
                            ],
                            "phones": [],
                            "best_name": "Roey F Horns"
                        },
                        {
                            "id": {
                                "key": "Person.3c812ed6-4319-44de-b573-c458e4346c9c.Durable",
                                "url": "https://proapi.whitepages.com/2.1/"
                                       "entity/Person.3c812ed6-4319-44de-b573-c458e4346c9c.Durable.json?api_key=KEYVAL",
                                "type": "Person",
                                "uuid": "3c812ed6-4319-44de-b573-c458e4346c9c",
                                "durability": "Durable"
                            },
                            "valid_for": {
                                "start": {
                                    "year": 2011,
                                    "month": 6,
                                    "day": 28
                                },
                                "stop": None
                            },
                            "type": "Full",
                            "names": [
                                {
                                    "salutation": None,
                                    "first_name": "Andrea",
                                    "middle_name": None,
                                    "last_name": "Horns",
                                    "suffix": None,
                                    "valid_for": None
                                }
                            ],
                            "age_range": {
                                "start": 45,
                                "end": 49
                            },
                            "gender": "Female",
                            "locations": [
                                {
                                    "id": {
                                        "key": "Location.efe46385-b057-40c3-8b67-f5a5278e0710.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity"
                                               "/Location.efe46385-b057-40c3-8b67-f5a5278e0710.Durable.json?"
                                               "api_key=KEYVAL",
                                        "type": "Location",
                                        "uuid": "efe46385-b057-40c3-8b67-f5a5278e0710",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Home",
                                    "type": "Address",
                                    "legal_entities_at": None,
                                    "city": "Seattle",
                                    "postal_code": "98119",
                                    "zip4": "3045",
                                    "state_code": "WA",
                                    "country_code": "US",
                                    "address": "402 W Howe St, Seattle WA 98119-3045",
                                    "house": "402",
                                    "street_name": "Howe",
                                    "street_type": "St",
                                    "apt_type": None,
                                    "is_receiving_mail": True,
                                    "not_receiving_mail_reason": None,
                                    "usage": "Residential",
                                    "delivery_point": "SingleUnit",
                                    "box_type": None,
                                    "address_type": "Street",
                                    "lat_long": {
                                        "latitude": 47.636105,
                                        "longitude": -122.362549,
                                        "accuracy": "RoofTop"
                                    },
                                    "is_deliverable": True,
                                    "contained_by_locations": None
                                }
                            ],
                            "phones": [],
                            "best_name": "Andrea Horns"
                        },
                        {
                            "id": {
                                "key": "Business.d2a27cbc-4760-49f5-99f3-65cac7911716.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity"
                                       "/Business.d2a27cbc-4760-49f5-99f3-65cac7911716.Durable.json?api_key=KEYVAL",
                                "type": "Business",
                                "uuid": "d2a27cbc-4760-49f5-99f3-65cac7911716",
                                "durability": "Durable"
                            },
                            "valid_for": None,
                            "name": "Andrea Horns Photography",
                            "locations": [
                                {
                                    "id": {
                                        "key": "Location.efe46385-b057-40c3-8b67-f5a5278e0710.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Location.efe46385-b057-40c3-8b67-f5a5278e0710.Durable.json?"
                                               "api_key=KEYVAL",
                                        "type": "Location",
                                        "uuid": "efe46385-b057-40c3-8b67-f5a5278e0710",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "type": "Address",
                                    "legal_entities_at": None,
                                    "city": "Seattle",
                                    "postal_code": "98119",
                                    "zip4": "3045",
                                    "state_code": "WA",
                                    "country_code": "US",
                                    "address": "402 W Howe St, Seattle WA 98119-3045",
                                    "house": "402",
                                    "street_name": "Howe",
                                    "street_type": "St",
                                    "apt_type": None,
                                    "is_receiving_mail": True,
                                    "not_receiving_mail_reason": None,
                                    "usage": "Residential",
                                    "delivery_point": "SingleUnit",
                                    "box_type": None,
                                    "address_type": "Street",
                                    "lat_long": {
                                        "latitude": 47.636105,
                                        "longitude": -122.362549,
                                        "accuracy": "RoofTop"
                                    },
                                    "is_deliverable": True,
                                    "contained_by_locations": None
                                }
                            ],
                            "phones": [
                                {
                                    "id": {
                                        "key": "Phone.c81d6fef-a2df-4b08-cfe3-bc7128b6f5f1.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Phone.c81d6fef-a2df-4b08-cfe3-bc7128b6f5f1.Durable.json?api_key=KEYVAL",
                                        "type": "Phone",
                                        "uuid": "c81d6fef-a2df-4b08-cfe3-bc7128b6f5f1",
                                        "durability": "Durable"
                                    },
                                    "contact_type": "Business",
                                    "line_type": "Landline",
                                    "belongs_to": None,
                                    "associated_locations": None,
                                    "is_valid": None,
                                    "phone_number": "2063131662",
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
                    "city": "Seattle",
                    "postal_code": "98119",
                    "zip4": "2043",
                    "state_code": "WA",
                    "country_code": "US",
                    "address": "413 W Howe St, Seattle WA 98119-2043",
                    "house": "413",
                    "street_name": "Howe",
                    "street_type": "St",
                    "apt_type": None,
                    "is_receiving_mail": True,
                    "not_receiving_mail_reason": None,
                    "usage": "Residential",
                    "delivery_point": "SingleUnit",
                    "box_type": None,
                    "address_type": "Street",
                    "lat_long": {
                        "latitude": 47.636105,
                        "longitude": -122.362549,
                        "accuracy": "RoofTop"
                    },
                    "is_deliverable": True
                }
            ],
            "messages": []
        }

        def test_location(self):
            location_test = [WhitePagesLocation(location) for location in self['results']]
            self.assertEqual(location_test[0].city, 'Seattle')
            self.assertEqual(location_test[0].is_deliverable, True)
