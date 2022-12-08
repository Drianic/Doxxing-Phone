import os
import phonenumbers
import opencage
from phonenumbers import geocoder

os.system("figlet Doxxing|lolcat")
os.system("figlet Phone|lolcat")
os.system("echo 'By Drianic'|lolcat")
print(" ")

number = input("por favor coloque un numero:" )

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print("localizacion:",location)

from phonenumbers import carrier
service_pro =phonenumbers.parse(number)
print("operadora:", carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = '023d51d96dc148f698e8430fca860270'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat =results [0]['geometry']['lat']
lng =results [0]['geometry']['lng']

print ("latitud:",lat,"longitud:",lng)





