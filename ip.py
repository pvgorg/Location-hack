import requests

def get_location(ip_address):
    url = 'http://ip-api.com/json/' + ip_address
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        location = f"IP: {ip_address}\nCountry: {data['country']}\nCity: {data['city']}\nLatitude: {data['lat']}\nLongitude: {data['lon']}"
        return location
    else:
        return 'Unable to retrieve location information.'

ip_address = input('Enter IP address: ')
location = get_location(ip_address)
print(location)
