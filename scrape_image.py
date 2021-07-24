import io

import requests
from PIL import Image
from bs4 import BeautifulSoup

BASE_URL = "https://scraping-for-beginner.herokuapp.com"
res = requests.get(BASE_URL+"/image")
soup = BeautifulSoup(res.text, "html.parser")
img_tags = soup.find_all("img")

for i, img_tag in enumerate(img_tags):
    img_url = BASE_URL + img_tag["src"]
    img = io.BytesIO(requests.get(img_url).content)  # url -> img
    img = Image.open(img)
    img.save(f"img/sample_{i}.png")
