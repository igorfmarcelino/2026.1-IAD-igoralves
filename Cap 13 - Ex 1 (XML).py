import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()

    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)

    results = tree.findall('result')

    if len(results) == 0:
        print("Nenhum resultado encontrado.")
        continue

    lat = results[0].find('geometry/location/lat').text
    lng = results[0].find('geometry/location/lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)

    country_code = None

    for component in results[0].findall('address_component'):
        tipos = component.findall('type')

        for tipo in tipos:
            if tipo.text == 'country':
                country_code = component.find('short_name').text
                break

        if country_code:
            break

    if country_code:
        print("Código do país:", country_code)
    else:
        print("Código do país: não disponível")