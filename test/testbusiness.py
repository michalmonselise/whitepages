from unittest2 import TestCase

from business import WhitePagesBusiness


class TestWhitePagesBusiness(TestCase):
    def setUp(self):
        self.basic_input = {
            "results": [
                {
                    "id": {
                        "key": "Business.b5b36dfd-dfb3-4700-9cdc-fc736fa7b43c.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Business.b5b36dfd-dfb3-4700-9cdc-fc736fa7b43c.Durable.json?api_key=KEYVAL",
                        "type": "Business",
                        "uuid": "b5b36dfd-dfb3-4700-9cdc-fc736fa7b43c",
                        "durability": "Durable"
                    },
                    "name": "Michaels Toyota",
                    "locations": [
                        {
                            "id": {
                                "key": "Location.4a5e6fd5-f3fc-47de-bf04-0226ae14f721.Ephemeral",
                                "url": None,
                                "type": "Location",
                                "uuid": "4a5e6fd5-f3fc-47de-bf04-0226ae14f721",
                                "durability": "Ephemeral"
                            },
                            "contact_type": None,
                            "type": "Address",
                            "legal_entities_at": [
                                {
                                    "id": {
                                        "key": "Business.b5b36dfd-dfb3-4700-9cdc-fc736fa7b43c.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Business.b5b36dfd-dfb3-4700-9cdc-fc736fa7b43c.Durable.json?"
                                               "api_key=KEYVAL",
                                        "type": "Business",
                                        "uuid": "b5b36dfd-dfb3-4700-9cdc-fc736fa7b43c",
                                        "durability": "Durable"
                                    },
                                    "valid_for": None,
                                    "name": "Michaels Toyota",
                                    "locations": None,
                                    "phones": [
                                        {
                                            "id": {
                                                "key": "Phone.261b6fef-a2df-4b08-cfe3-bc7128b6f5d5.Durable",
                                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                                       "Phone.261b6fef-a2df-4b08-cfe3-bc7128b6f5d5.Durable.json?"
                                                       "api_key=KEYVAL",
                                                "type": "Phone",
                                                "uuid": "261b6fef-a2df-4b08-cfe3-bc7128b6f5d5",
                                                "durability": "Durable"
                                            },
                                            "contact_type": "Business"
                                        }
                                    ]
                                }
                            ],
                            "city": "Seattle",
                            "postal_code": "98125",
                            "zip4": None,
                            "state_code": "WA",
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
                                "latitude": 47.714686676788,
                                "longitude": -122.307876687081,
                                "accuracy": None
                            },
                            "is_deliverable": None
                        }
                    ],
                    "phones": [
                        {
                            "id": {
                                "key": "Phone.261b6fef-a2df-4b08-cfe3-bc7128b6f5d5.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.261b6fef-a2df-4b08-cfe3-bc7128b6f5d5.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "261b6fef-a2df-4b08-cfe3-bc7128b6f5d5",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "2062193421",
                            "country_calling_code": "1",
                            "extension": None,
                            "carrier": None,
                            "do_not_call": None,
                            "reputation": None,
                            "is_prepaid": None,
                            "best_location": None
                        }
                    ]
                },
                {
                    "id": {
                        "key": "Business.2655de5d-72d0-424b-bdb6-5d9753dba0f2.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Business.2655de5d-72d0-424b-bdb6-5d9753dba0f2.Durable.json?api_key=KEYVAL",
                        "type": "Business",
                        "uuid": "2655de5d-72d0-424b-bdb6-5d9753dba0f2",
                        "durability": "Durable"
                    },
                    "name": "Toyota Of Lake City",
                    "locations": [
                        {
                            "id": {
                                "key": "Location.2d7b7a78-9031-4a65-8d34-097d8129fc9b.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Location.2d7b7a78-9031-4a65-8d34-097d8129fc9b.Durable.json?api_key=KEYVAL",
                                "type": "Location",
                                "uuid": "2d7b7a78-9031-4a65-8d34-097d8129fc9b",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "type": "Address",
                            "legal_entities_at": None,
                            "city": "Seattle",
                            "postal_code": "98125",
                            "zip4": "4430",
                            "state_code": "WA",
                            "country_code": "US",
                            "address": "13355 Lake City Way NE, Seattle, WA 98125-4430",
                            "house": "13355",
                            "street_name": "Lake City",
                            "street_type": "Way",
                            "apt_type": None,
                            "is_receiving_mail": True,
                            "not_receiving_mail_reason": None,
                            "usage": "Business",
                            "delivery_point": "SingleUnit",
                            "box_type": None,
                            "address_type": "Street",
                            "lat_long": {
                                "latitude": 47.726143,
                                "longitude": -122.293465,
                                "accuracy": "RoofTop"
                            },
                            "is_deliverable": True
                        }
                    ],
                    "phones": [
                        {
                            "id": {
                                "key": "Phone.f1f16fef-a2e2-4b08-cfe3-bc7128b4238d.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.f1f16fef-a2e2-4b08-cfe3-bc7128b4238d.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "f1f16fef-a2e2-4b08-cfe3-bc7128b4238d",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "8888187128",
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
                                "key": "Phone.fff96fef-a2df-4b08-cfe3-bc7128b6f601.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.fff96fef-a2df-4b08-cfe3-bc7128b6f601.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "fff96fef-a2df-4b08-cfe3-bc7128b6f601",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "2063663100",
                            "country_calling_code": "1",
                            "extension": None,
                            "carrier": None,
                            "do_not_call": None,
                            "reputation": None,
                            "is_prepaid": None,
                            "best_location": None
                        }
                    ]
                },
                {
                    "id": {
                        "key": "Business.137927e8-ac94-4450-8fe3-ae2bd6afefa3.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Business.137927e8-ac94-4450-8fe3-ae2bd6afefa3.Durable.json?api_key=KEYVAL",
                        "type": "Business",
                        "uuid": "137927e8-ac94-4450-8fe3-ae2bd6afefa3",
                        "durability": "Durable"
                    },
                    "name": "Linda Tenney Toyota",
                    "locations": [
                        {
                            "id": {
                                "key": "Location.2d7b7a78-9031-4a65-8d34-097d8129fc9b.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Location.2d7b7a78-9031-4a65-8d34-097d8129fc9b.Durable.json?api_key=KEYVAL",
                                "type": "Location",
                                "uuid": "2d7b7a78-9031-4a65-8d34-097d8129fc9b",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "type": "Address",
                            "legal_entities_at": None,
                            "city": "Seattle",
                            "postal_code": "98125",
                            "zip4": "4430",
                            "state_code": "WA",
                            "country_code": "US",
                            "address": "13355 Lake City Way NE, Seattle, WA 98125-4430",
                            "house": "13355",
                            "street_name": "Lake City",
                            "street_type": "Way",
                            "apt_type": None,
                            "is_receiving_mail": True,
                            "not_receiving_mail_reason": None,
                            "usage": "Business",
                            "delivery_point": "SingleUnit",
                            "box_type": None,
                            "address_type": "Street",
                            "lat_long": {
                                "latitude": 47.726143,
                                "longitude": -122.293465,
                                "accuracy": "RoofTop"
                            },
                            "is_deliverable": True
                        }
                    ],
                    "phones": [
                        {
                            "id": {
                                "key": "Phone.36816fef-a2df-4b08-cfe3-bc7128b6f602.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.36816fef-a2df-4b08-cfe3-bc7128b6f602.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "36816fef-a2df-4b08-cfe3-bc7128b6f602",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "2063670080",
                            "country_calling_code": "1",
                            "extension": None,
                            "carrier": None,
                            "do_not_call": None,
                            "reputation": None,
                            "is_prepaid": None,
                            "best_location": None
                        }
                    ]
                },
                {
                    "id": {
                        "key": "Business.71072cf1-5345-46bb-a05b-e67a79f051ba.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Business.71072cf1-5345-46bb-a05b-e67a79f051ba.Durable.json?api_key=KEYVAL",
                        "type": "Business",
                        "uuid": "71072cf1-5345-46bb-a05b-e67a79f051ba",
                        "durability": "Durable"
                    },
                    "name": "Toyota Of Lake City",
                    "locations": [
                        {
                            "id": {
                                "key": "Location.4586c16a-711b-4f6d-af78-879aafcaa2a4.Ephemeral",
                                "url": None,
                                "type": "Location",
                                "uuid": "4586c16a-711b-4f6d-af78-879aafcaa2a4",
                                "durability": "Ephemeral"
                            },
                            "contact_type": None,
                            "type": "Address",
                            "legal_entities_at": [
                                {
                                    "id": {
                                        "key": "Business.71072cf1-5345-46bb-a05b-e67a79f051ba.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Business.71072cf1-5345-46bb-a05b-e67a79f051ba.Durable.json?"
                                               "api_key=KEYVAL",
                                        "type": "Business",
                                        "uuid": "71072cf1-5345-46bb-a05b-e67a79f051ba",
                                        "durability": "Durable"
                                    },
                                    "valid_for": None,
                                    "name": "Toyota Of Lake City",
                                    "locations": None,
                                    "phones": [
                                        {
                                            "id": {
                                                "key": "Phone.009f6fef-a2df-4b08-cfe3-bc7128b6f602.Durable",
                                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                                       "Phone.009f6fef-a2df-4b08-cfe3-bc7128b6f602.Durable.json?"
                                                       "api_key=KEYVAL",
                                                "type": "Phone",
                                                "uuid": "009f6fef-a2df-4b08-cfe3-bc7128b6f602",
                                                "durability": "Durable"
                                            },
                                            "contact_type": "Business"
                                        }
                                    ]
                                }
                            ],
                            "city": "Seattle",
                            "postal_code": "98125",
                            "zip4": None,
                            "state_code": "WA",
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
                                "latitude": 47.726768,
                                "longitude": -122.292671,
                                "accuracy": None
                            },
                            "is_deliverable": None
                        }
                    ],
                    "phones": [
                        {
                            "id": {
                                "key": "Phone.009f6fef-a2df-4b08-cfe3-bc7128b6f602.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.009f6fef-a2df-4b08-cfe3-bc7128b6f602.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "009f6fef-a2df-4b08-cfe3-bc7128b6f602",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "2063663183",
                            "country_calling_code": "1",
                            "extension": None,
                            "carrier": None,
                            "do_not_call": None,
                            "reputation": None,
                            "is_prepaid": None,
                            "best_location": None
                        }
                    ]
                },
                {
                    "id": {
                        "key": "Business.75341f27-6ab9-49f9-a7ed-16c70e53758f.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Business.75341f27-6ab9-49f9-a7ed-16c70e53758f.Durable.json?api_key=KEYVAL",
                        "type": "Business",
                        "uuid": "75341f27-6ab9-49f9-a7ed-16c70e53758f",
                        "durability": "Durable"
                    },
                    "name": "Toyota Of Lake City",
                    "locations": [
                        {
                            "id": {
                                "key": "Location.8a6c3fee-d0b4-48dc-8575-05d7ec8d8de3.Ephemeral",
                                "url": None,
                                "type": "Location",
                                "uuid": "8a6c3fee-d0b4-48dc-8575-05d7ec8d8de3",
                                "durability": "Ephemeral"
                            },
                            "contact_type": None,
                            "type": "Address",
                            "legal_entities_at": [
                                {
                                    "id": {
                                        "key": "Business.75341f27-6ab9-49f9-a7ed-16c70e53758f.Durable",
                                        "url": "https://proapi.whitepages.com/2.1/entity/"
                                               "Business.75341f27-6ab9-49f9-a7ed-16c70e53758f.Durable.json?"
                                               "api_key=KEYVAL",
                                        "type": "Business",
                                        "uuid": "75341f27-6ab9-49f9-a7ed-16c70e53758f",
                                        "durability": "Durable"
                                    },
                                    "valid_for": None,
                                    "name": "Toyota Of Lake City",
                                    "locations": None,
                                    "phones": [
                                        {
                                            "id": {
                                                "key": "Phone.6d056fef-a2df-4b08-cfe3-bc7128b6f601.Durable",
                                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                                       "Phone.6d056fef-a2df-4b08-cfe3-bc7128b6f601.Durable.json?"
                                                       "api_key=KEYVAL",
                                                "type": "Phone",
                                                "uuid": "6d056fef-a2df-4b08-cfe3-bc7128b6f601",
                                                "durability": "Durable"
                                            },
                                            "contact_type": "Business"
                                        }
                                    ]
                                }
                            ],
                            "city": "Seattle",
                            "postal_code": "98125",
                            "zip4": None,
                            "state_code": "WA",
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
                                "latitude": 47.716999,
                                "longitude": -122.297119,
                                "accuracy": None
                            },
                            "is_deliverable": None
                        }
                    ],
                    "phones": [
                        {
                            "id": {
                                "key": "Phone.6d056fef-a2df-4b08-cfe3-bc7128b6f601.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.6d056fef-a2df-4b08-cfe3-bc7128b6f601.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "6d056fef-a2df-4b08-cfe3-bc7128b6f601",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "2063644290",
                            "country_calling_code": "1",
                            "extension": None,
                            "carrier": None,
                            "do_not_call": None,
                            "reputation": None,
                            "is_prepaid": None,
                            "best_location": None
                        }
                    ]
                },
                {
                    "id": {
                        "key": "Business.17878b3e-70c5-4961-9ebd-aa00bc556030.Durable",
                        "url": "https://proapi.whitepages.com/2.1/entity/"
                               "Business.17878b3e-70c5-4961-9ebd-aa00bc556030.Durable.json?api_key=KEYVAL",
                        "type": "Business",
                        "uuid": "17878b3e-70c5-4961-9ebd-aa00bc556030",
                        "durability": "Durable"
                    },
                    "name": "Toyota/scion Of Seattle",
                    "locations": [
                        {
                            "id": {
                                "key": "Location.f07f59cf-70ef-4e29-af05-004fc3bf8c66.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Location.f07f59cf-70ef-4e29-af05-004fc3bf8c66.Durable.json?api_key=KEYVAL",
                                "type": "Location",
                                "uuid": "f07f59cf-70ef-4e29-af05-004fc3bf8c66",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "type": "Address",
                            "legal_entities_at": None,
                            "city": "Seattle",
                            "postal_code": "98121",
                            "zip4": "2607",
                            "state_code": "WA",
                            "country_code": "US",
                            "address": "2121 8th Ave, Seattle, WA 98121-2607",
                            "house": "2121",
                            "street_name": "8th",
                            "street_type": "Ave",
                            "apt_type": None,
                            "is_receiving_mail": True,
                            "not_receiving_mail_reason": None,
                            "usage": "Business",
                            "delivery_point": "SingleUnit",
                            "box_type": None,
                            "address_type": "Street",
                            "lat_long": {
                                "latitude": 47.616833,
                                "longitude": -122.339081,
                                "accuracy": "RoofTop"
                            },
                            "is_deliverable": True
                        }
                    ],
                    "phones": [
                        {
                            "id": {
                                "key": "Phone.5ae76fef-a2e1-4b08-cfe3-bc7128b7ba1a.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.5ae76fef-a2e1-4b08-cfe3-bc7128b7ba1a.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "5ae76fef-a2e1-4b08-cfe3-bc7128b7ba1a",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "8003595635",
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
                                "key": "Phone.eb596fef-a2df-4b08-cfe3-bc7128b6f606.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.eb596fef-a2df-4b08-cfe3-bc7128b6f606.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "eb596fef-a2df-4b08-cfe3-bc7128b6f606",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "2063824300",
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
                                "key": "Phone.5ae76fef-a2e1-4b08-cfe3-bc7128b7ba1a.Durable",
                                "url": "https://proapi.whitepages.com/2.1/entity/"
                                       "Phone.5ae76fef-a2e1-4b08-cfe3-bc7128b7ba1a.Durable.json?api_key=KEYVAL",
                                "type": "Phone",
                                "uuid": "5ae76fef-a2e1-4b08-cfe3-bc7128b7ba1a",
                                "durability": "Durable"
                            },
                            "contact_type": "Business",
                            "line_type": "Landline",
                            "belongs_to": None,
                            "associated_locations": None,
                            "is_valid": None,
                            "phone_number": "8003595635",
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
            "messages": []
        }

        def test_business(self):
            business_test = [WhitePagesBusiness(business) for business in self['results']]
            self.assertEqual(business_test[0].name, 'Michaels Toyota')
            self.assertEqual(len(business_test[0].locations), 1)