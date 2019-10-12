 from urllib import request

import json

from os import *

system("clear")
system("figlet IP Location | lolcat")
print ("==============================")
print ("| Author : ./Xmuezza         |")
print ("| Team   : XaiSyndicate      |")
print ("==============================")
ip = input('Masukkan IP Anda : ')
api = 'http://ip-api.com/json/'+ip
resp = request.urlopen(api)
data = json.loads(resp.read())
print ("[+] Status \t: "+data["status"])
print ("[+] As \t\t: "+data["as"])
print ("[+] City \t: "+data["city"])
print ("[+] Country \t: "+data["country"])
print ("[+] CountryCode : "+data["countryCode"])
print ("[+] Isp \t: "+data["isp"])
lat = print ("[+] Lat \t: "+str(data["lat"]))
lon = print ("[+] Lon \t: "+str(data["lon"]))
print ("[+] RegionName \t: "+data["regionName"])
print ("[+] Timezone \t: "+data["timezone"])
print ("[+] Link Googlemap Anda : https://maps.google.com/?q=",str(data["lat"]),str(data["lon"]))
