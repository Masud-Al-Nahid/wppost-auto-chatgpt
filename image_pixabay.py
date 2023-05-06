

def pixabay_img(query,alt):
    from requests import get
    api_key = "1467657-335c1a30779a1369ca85f13dc"
    api_url = f'https://pixabay.com/api/?key={api_key}&q={query}&image_type=photo'
    r= get(api_url).json()
    api_data =r.get('hits')[1].get('webformatURL')
    wp_img = f"<img class='img-fluid' src="{api_data}" alt="{alt}" width="960" height="640"/>"
    return wp_img