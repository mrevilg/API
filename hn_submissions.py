import requests

from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/vO/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)