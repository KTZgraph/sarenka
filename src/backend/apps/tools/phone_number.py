"""
source: https://www.youtube.com/watch?v=sT_MJKqlupk
"""
from phonenumbers import carrier, geocoder, parse

phone_nr = "+48616652945"
number = parse(phone_nr)

# miasto/kraj
phone_country = geocoder.description_for_number(number, 'en')
print(phone_country)


#siec telefonu
phone_carrier = carrier.name_for_number(number, 'en')
print(phone_carrier)
