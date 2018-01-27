import requests
from bs4 import BeautifulSoup as bs
import os

#The website that images will be scraped from
url = 'https://www.pexels.com/search/model/'

# download page for scraping
page = requests.get(url)
soup = bs(page.text, 'html.parser')


# find all images with a specific tag
image_tags = soup.findAll('img')

# Check if the folder that will store the scraped images exists
if not os.path.exists('models'):
    os.makedirs('models')

# move to the new directory
os.chdir('models')

# image file name variable
x = 0

# writing images to the folder
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass



