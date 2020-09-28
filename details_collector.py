import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import phonemetadata

ph_num = phonenumbers.parse('+919562433164')

print(geocoder.description_for_number(ph_num, 'en'))
print(carrier.name_for_number(ph_num, 'en'))
print(phonemetadata.NumberFormat(ph_num, 'en'))