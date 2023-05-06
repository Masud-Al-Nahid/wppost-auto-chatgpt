import requests

# Define the API endpoint URL
url = 'https://spotify.local/wp-json/wp/v2/media'
url_slug ='the-agency-summit'
per_page = '20'
# Set the query parameters to filter the image you want
params = {
    'search': url_slug,
    'per_page': per_page,
}

# Send a GET request to the API endpoint
response = requests.get(url, params=params, verify=False)

# Extract the image ID from the response
image_id = response.json()[0]['id']

print(f'The image ID is: {image_id}')
