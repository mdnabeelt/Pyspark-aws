from faker import Faker
fake = Faker()

location_source = list(fake.location_on_land())
#print(location_source)
date = fake.date()

print("advertising_id :-", fake.pystr())
print("city :-", location_source[2])
print("location_category :-", location_source[4])
print("location_granularities :-", fake.street_name())
print("location_source :-", location_source[2:])
print("state :-", location_source[-1].split('/')[1])
print("timestamp :-", fake.unix_time())
print("user_id :-", fake.pystr())
print("user_latitude :-", location_source[0])
print("user_longitude :-", location_source[1])
print("month :-", date.split('-')[1])
print("date :-", date)
