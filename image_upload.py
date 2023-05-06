import requests

image_name = 'blog-post'
# Set the URL of the WordPress REST API endpoint for media uploads
url = "https://spotify.local/wp-json/wp/v2/media"

# Set the path to the image file you want to upload
image_path = "C:\Users\mdmsd2\Desktop\Test-code/blog-post.jpg"

# Open the image file and read its contents
with open(f'images/' + {image_name} + '.jpg', "rb", encoding='utf-8' ) as image_file:
    image_data = image_file.read()

# Set the headers for the HTTP request
headers = {
    "Content-Disposition": "attachment; filename=image.jpg",
    "Content-Type": "image/jpeg"
}

# Make the HTTP request to upload the image to the media library
response = requests.post(url, headers=headers, data=image_data)

# Print the response from the server
print(response.json())

