import requests

# set the URL of the WordPress site and the post slug
url = "https://hotcalculator.com/wp-json/wp/v2/posts"
slug = "how-to-convert-celsius-into-fahrenheit-in-omron-digital-thermometer"

# make the request to the WordPress REST API
response = requests.get(url, params={"slug": slug})

# check if the response was successful
if response.status_code != 200:
    print("Error: Failed to retrieve post ID")
    exit()

# extract the post ID from the response
post_id = response.json()[0]["id"]

# print the post ID
print("Post ID:", post_id)
