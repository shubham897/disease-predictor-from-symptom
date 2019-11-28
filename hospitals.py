import requests, json
api_key = 'AIzaSyDfnjbBIqMVUJWAZ5HoFH8aNftrSbn2egk'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
query = input('Search query: ')
r = requests.get(url + 'query=' + query +
                 '&key=' + api_key)
x = r.json()
y = x['results']
for i in range(len(y)):
    print(y[i]['name'])