import requests
from requests import get
import shutil
from PIL import Image
import base64
import os
import random
import json
from chat_ai import chat_gptai
from wp_fungs import  wp_h2, text_formatting, wp_headers
from people_also import get_people_also_ask
# from image import pixabay_image_operation, body_img
from pixabay_img_url import pixabay_1st_img, wp_image_url,pixabay_ppa_img
from ppa_text import ppa

web_site_url = 'https://www.seeandroid.com'

with open('keywords.txt', 'r') as file:
    readline = file.readlines()
    for line in readline:
        keyword_slug = line.replace(' ','-').strip()
        keyword_img_slug =line.replace(' ','+').strip()
        
        prompt =f"Write a short eye-catchy SEO optimized blog post title with exacting keywords about + {line}"
        title =chat_gptai(prompt).replace('"',' ')
        wp_title = title.title()

        prompt = f"Write a short SEO optimized introduction with exacting keywords about + {line}+ within 100 words"
        intro_ai = chat_gptai(prompt)
        wp_intro = text_formatting(intro_ai)
        
        prompt = f"Write a short SEO optimized blog post headline with exact about + {line}"
        first_h2 = chat_gptai(prompt).replace('"',' ')
        second_h2 = wp_h2(first_h2)
    
        prompt = f"Write a long explanation of + {line} + and use multiple short paragraph with 500 word"
        articles = chat_gptai(prompt)
        wp_articles = text_formatting(articles)
        
        file=ppa()
        ppa_wp_h2 = wp_h2(file)
        
        
        prompt = f"Write a medium explanation of + {file} + and use multiple short paragraph with 200 word"
        ppa_articles = chat_gptai(prompt)
        ppa_wp_content = text_formatting(ppa_articles)
        
        conclusion_title = wp_h2("Conclusion")
        
        prompt = f"Write a short SEO optimized blog post summary with exact about+{line}+ with 50 words"
        conclusion = chat_gptai(prompt)
        wp_conclusion = text_formatting(conclusion)
        
        # photos = media_upload('this is test.jpg', line)
        # ppa_photos = pixabay_img(ppa)
        
        image_url = pixabay_1st_img()
        first_photo_url = wp_image_url(image_url,line)
        
        
        ppa_image= pixabay_ppa_img()
        ppa_image_url = wp_image_url(ppa_image,file)
        
        content =f'{wp_intro}{second_h2}{first_photo_url}{wp_articles}{ppa_wp_h2}{ppa_image_url}{ppa_wp_content}{conclusion_title}{wp_conclusion}'
        
        # featured image start
        directory = 'images'
        if not os.path.exists(directory):
            os.makedirs(directory)
        api_key = "1467657-335c1a30779a1369ca85f13dc"
        query = input('Type your search keyword: ').replace(' ','+').strip()
        api_url = f'https://pixabay.com/api/?key={api_key}&q={query}&image_type=photo'
        r= get(api_url).json()
        api_data = r.get('hits')
        for data in api_data:
            img_url = data.get('webformatURL')
            file =open('images/' + keyword_slug + '.jpg', 'wb')
            file.write(get(img_url).content)
            file.close()
            
        media_url = 'https://www.seeandroid.com/wp-json/wp/v2/media'
        files = {'file': open('images/' + keyword_slug + '.jpg', 'rb')}
        headers = wp_headers('mdmsd2', 'utdk xfNz 9ot5 6EUc UIct CSrZ')
        res = requests.post(media_url, headers=headers, files=files, verify=False)
        data = res.json()
        id = data.get('id')
        src = data.get('guid').get('rendered')

        # Define the API endpoint URL
        url = 'https://www.seeandroid.com/wp-json/wp/v2/media'
        url_slug =keyword_slug
        per_page = '20'
        # Set the query parameters to filter the image you want
        params = {
            'search': url_slug,
            'per_page': per_page,
            'name': line,
        }

        # Send a GET request to the API endpoint
        response = requests.get(url, params=params)

        # Extract the image ID from the response
        image_id = response.json()[0]['id']
        
        # Featured image end

        featured_id = image_id
        
        data = {
            'slug': keyword_slug,
            'title': wp_title,
            'content': content,
            'categories': 5,
            'status': 'publish',
            'format': 'standard',
            'featured_media': featured_id
        }
        
        headers = wp_headers('mdmsd2', 'utdk xfNz 9ot5 6EUc UIct CSrZ')
        post_url = 'https://www.seeandroid.com/wp-json/wp/v2/posts'
        response=requests.post(post_url, data=data, headers=headers)
        if response.status_code == 201:
            print(web_site_url +'/'+ keyword_slug + ' Has Been Posted created successfully')
        else:
            print("Error creating category:", response.text)
    