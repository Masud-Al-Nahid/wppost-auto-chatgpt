from requests import get
import json
import os
from wp_fungs import wp_headers
directory = 'images'
if not os.path.exists(directory):
    os.makedirs(directory)
api_key = "1467657-335c1a30779a1369ca85f13dc"
quary = 'blog post'
image_name = quary.replace(' ', '-')
quary_slug = quary.replace(' ', '+')
api_url = f'https://pixabay.com/api/?key={api_key}&q={quary_slug}&image_type=photo'
r= get(api_url).json()
api_data = r.get('hits')
for data in api_data:
    img_url = data.get('webformatURL')
    file =open('images/' + image_name + '.jpg', 'wb')
    file.write(get(img_url).content)
    file.close()
    

import requests
media_url = 'https://spotify.local/wp-json/wp/v2/media'
files = {'file': open('images/' + image_name + '.jpg', 'rb')}
headers = wp_headers('mdmsd2', 'aQNC NJuF cccO tzfw uNLV W1dA')
res = requests.post(media_url, headers=headers, files=files, verify=False)
data = res.json()
id = data.get('id')
src = data.get('guid').get('rendered')

# Define the API endpoint URL
url = 'https://spotify.local/wp-json/wp/v2/media'
url_slug =image_name
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

