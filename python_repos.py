import requests

# Make an API sand store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API in a variable.
response_dict = r.json()
print("Total Repositories:", response_dict['total_count'])

# Explore information about repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examin first repo
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
