import requests

from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/vO/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submissions_ids = r.json()
submissions_dicts = []
for submissions_id in submissions_ids[:30]:
    # Make a seperate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/vO/item/' + 
            str(submissions_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()