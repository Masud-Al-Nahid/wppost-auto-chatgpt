 
def pixabay_1st_img():
    from requests import get
    api_key = "1467657-335c1a30779a1369ca85f13dc"
    with open('ppa_img.txt','r') as file:
        readline = file.readlines()
        for line in readline:
            f_text = line.strip()
            api_url = f'https://pixabay.com/api/?key={api_key}&q={f_text}&image_type=photo'
            r= get(api_url).json()
            api_data =r.get('hits')[1].get('webformatURL')
            return api_data

def pixabay_ppa_img():
    from requests import get
    api_key = "1467657-335c1a30779a1369ca85f13dc"
    with open('ppa_img.txt','r') as file:
        readline = file.readlines()
        for line in readline:
            f_text = line.strip()
            api_url = f'https://pixabay.com/api/?key={api_key}&q={f_text}&image_type=photo'
            r= get(api_url).json()
            api_data =r.get('hits')[2].get('webformatURL')
            return api_data


def wp_image_url(src, alt):
    first_line = '<!--wp:image{"sizeSlug":"large", "width":703, "height":468}-->'
    second_line = f'<figure class="wp-block-image size-large"><img src="{src}" alt="{alt}"/>'
    third_line = '</figure><!--/wp:image-->'
    code = f'{first_line}{second_line}{third_line}'
    return code
