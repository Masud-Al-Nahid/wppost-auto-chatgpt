import requests

# Set the API endpoint URL and the tag name
url = 'https://spotify.local/wp-json/wp/v2/tags'
tag_name = 'music'

# Make the HTTP GET request to retrieve the list of tags
response = requests.get(url, verify=False)

# Loop through the list of tags and find the one with the matching name
for tag in response.json():
    if tag['name'] == tag_name:
        tag_id = tag['id']
        break

print(f"The ID of the {tag_name} tag is {tag_id}")
