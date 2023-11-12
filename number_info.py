import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter your number with +880: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(phone)
print()
print(time)
print()
print(car)
print()
print(reg)