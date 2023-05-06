

def wp_headers(username,password):
    import base64
    credentials = f"{username}:{password}"
    token = base64.b64encode(credentials.encode())
    code = {"Authorization": f"Basic {token.decode()}"}
    return code

# def pixabay_img(keyword):
#     import requests
#     import os
#     api_key = "1467657-335c1a30779a1369ca85f13dc"
#     if not os.path.exists('images'):
#         os.makedirs('images')
#     try:
#         quary = keyword
#     api_url = f'https://pixabay.com/api/?key={api_key}&q={quary}&image_type=photo'
#     r= requests.get(api_url).json()
#     src =r.get('hits')[1].get('webformatURL')
#     return src

def body_img(id,src, keyword):
    src = pixabay_img(keyword)
    first_line = f'<!-- wp:image {{"align":"center","id":{id},"sizeSlug":"full","linkDestination":"none", "width":703,"height":468}} -->'
    second_line = f'<figure class="wp-block-image aligncenter size-full"><img src="{src}" alt="{keyword}" class="wp-image-{id}"/>'
    third_line = '</figure><!-- /wp:image -->'
    code = f'{first_line}{second_line}{third_line}'
    return code

def media_upload(image,keyword):
    import requests
    media_url = 'https://spotify.local/wp-json/wp/v2/media'
    files = {'file': open('images/' + keyword + '.jpg', 'rb')}
    headers = wp_headers('mdmsd2', 'aQNC NJuF cccO tzfw uNLV W1dA')
    res = requests.post(media_url, headers=headers, files=files, verify=False)
    data = res.json()
    id = data.get('id')
    src = data.get('guid').get('rendered')
    image_code = body_img(id,src, keyword)
    return image_code


    

def wp_h2(text):
    return f"<!--wp:heading--><h2>{text}</h2><!--/wp:heading-->"

# def wp_para(text):
#     return f"<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->" 

# def wp_h3(text):
#     return f"<!-- wp:heading --><h3>{text}</h3><!-- /wp:heading -->"

# def text_formating(text):
#     text = text.replace('.', '.---').split('---')
#     retun_text1 = '<!-- wp:paragraph --><p>' + ''.join(text[0:3]) + '</p><!-- /wp:paragraph -->'
#     retun_text2 = '<!-- wp:paragraph --><p>' + ''.join(text[3:6]) + '</p><!-- /wp:paragraph -->'
#     retun_text3 = '<!-- wp:paragraph --><p>' + ''.join(text[6:]) + '</p><!-- /wp:paragraph -->'
#     return retun_text1 + retun_text2 + retun_text3

def text_formatting(text):
    text_segments = text.replace('.', '.---').split('---')
    return_text = ''
    for i in range(0, len(text_segments), 3):
        return_text += '<!--wp:paragraph--><p>' + ''.join(text_segments[i:i+3]) + '</p><!--/wp:paragraph -->'
    return return_text
