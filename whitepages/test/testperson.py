import unittest2 as unittest

from whitepages.person import WhitePagesPerson


class TestWhitePagesPerson(unittest.TestCase):
    def setUp(self):
        self.basic_input = {
            "results": [
                {
                    "id": {
                        "key": "Person.8e5f2f09-6755-4183-9a0b-a2be09f35756.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Person.8e5f2f09-6755-4183-9a0b-a2be09f35756.Durable.json?api_key=KEYVAL",
                        "type": "Person",
                        "uuid": "8e5f2f09-6755-4183-9a0b-a2be09f35756",
                        "durability": "Durable"
                    },
                    "type": "Full",
                    "names": [
                        {
                            "salutation": None,
                            "first_name": "Scott",
                            "middle_name": "A",
                            "last_name": "Sikora",
                            "suffix": None,
                            "valid_for": None
                        }
                    ],
                    "age_range": {
                        "start": 45,
                        "end": 49
                    },
                    "gender": "Male",
                    "locations": [
                        {
                            "id": {
                                "key": "Location.52d627cd-23ba-447e-9db8-e00866d33508.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Location.52d627cd-23ba-447e-9db8-e00866d33508.Durable.json?api_key=KEYVAL",
                                "type": "Location",
                                "uuid": "52d627cd-23ba-447e-9db8-e00866d33508",
                                "durability": "Durable"
                            },
                            "contact_type": "Home",
                            "type": "Address",
                            "legal_entities_at": [
                                {
                                    "id": {
                                        "key": "Person.ccc18d4f-3431-4336-bd9c-a3ca2e3980fc.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Person.ccc18d4f-3431-4336-bd9c-a3ca2e3980fc.Durable.json?"
                                               "api_key=KEYVAL",
                                        "type": "Person",
                                        "uuid": "ccc18d4f-3431-4336-bd9c-a3ca2e3980fc",
                                        "durability": "Durable"
                                    },
                                    "valid_for": None,
                                    "type": "Full",
                                    "names": [
                                        {
                                            "salutation": None,
                                            "first_name": "Stacy",
                                            "middle_name": "L",
                                            "last_name": "Sikora",
                                            "suffix": None,
                                            "valid_for": None
                                        }
                                    ],
                                    "age_range": {
                                        "start": 50,
                                        "end": 54
                                    },
                                    "gender": "Female",
                                    "locations": None,
                                    "phones": None,
                                    "best_name": "Stacy L Sikora",
                                    "best_location": None,
                                    "associated_people": None
                                },
                                {
                                    "id": {
                                        "key": "Person.8e5f2f09-6755-4183-9a0b-a2be09f35756.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Person.8e5f2f09-6755-4183-9a0b-a2be09f35756.Durable.json?"
                                               "api_key=KEYVAL",
                                        "type": "Person",
                                        "uuid": "8e5f2f09-6755-4183-9a0b-a2be09f35756",
                                        "durability": "Durable"
                                    },
                                    "valid_for": None,
                                    "type": "Full",
                                    "names": [
                                        {
                                            "salutation": None,
                                            "first_name": "Scott",
                                            "middle_name": "A",
                                            "last_name": "Sikora",
                                            "suffix": None,
                                            "valid_for": None
                                        }
                                    ],
                                    "age_range": {
                                        "start": 45,
                                        "end": 49
                                    },
                                    "gender": "Male",
                                    "locations": None,
                                    "phones": None,
                                    "best_name": "Scott A Sikora",
                                    "best_location": None,
                                    "associated_people": None
                                }
                            ],
                            "city": "Seattle",
                            "postal_code": "98119",
                            "zip4": "2134",
                            "state_code": "WA",
                            "country_code": "US",
                            "address": "413 E Howe St, Seattle WA 98119-2134",
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
                                "latitude": 47.635761,
                                "longitude": -122.362556,
                                "accuracy": "RoofTop"
                            },
                            "is_deliverable": True
                        }
                    ],
                    "phones": [],
                    "best_name": "Scott A Sikora"
                }
            ],
            "messages": []
        }

        def test_person(self):
            person_test = [WhitePagesPerson(person) for person in self['results']]
            self.assertEqual(person_test[0].best_name, 'Scott A Sikora')
            self.assertEqual(person_test[0].gender, 'Male')