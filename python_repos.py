import requests

# Make an API sand store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

#Store API in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())
