import requests
import json
import base64


wp_user= 'mdmsd2'
website_url = 'https://spotify.local'
wp_pass= 'aQNC NJuF cccO tzfw uNLV W1dA'
wp_credentials = f"{wp_user}:{wp_pass}"
wp_token = base64.b64encode(wp_credentials.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}', "Content-Type": "application/json"}


# Set the post data and meta fields
post_data = {
    "title": "Your post title",
    "content": "Your post content",
    "meta": {
        "your_meta_key": "Your meta value"
    }
}

url = website_url+"/wp-json/wp/v2/posts"
# Encode the data as JSON
json_data = json.dumps(post_data)

# Send the request
response = requests.post(url, data=json_data, headers=wp_headers, verify=False)

# Print the response
print(response.json())

