whitepages

This package is a wrapper for the White Pages API.

It enables us to perform 4 different kinds of searches: person, business, location (reverse address), and phone (reverse phone).
At the moment identity score is not enabled.

After obtaining a key, we can generate a WhitePages object and then perform a search.

For example:
    
	from whitepages import WhitePages
    w = WhitePages(key)
    person_result = w.person(name='Jane Smith')
	business_result = w.business(name="Michaels Toyota", city=Seattle")
	location_result = w.location(street_line_1="123 Broadway",city="New York", state="NY")
	phone_result = w.phone(phone_number="206-123-4567")
	


