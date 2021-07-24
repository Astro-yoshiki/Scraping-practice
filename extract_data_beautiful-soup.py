import requests
from bs4 import BeautifulSoup


URL = "https://scraping-for-beginner.herokuapp.com/udemy"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup.find_all("p"))
subscribers = soup.find_all("p", attrs={"class": "subscribers"})[0]
# other way: soup.select(".subscribers)
n_subscribers = int(subscribers.text.split("：")[1])

reviews = soup.find_all("p", attrs={"class": "reviews"})[0]
n_reviews = int(reviews.text.split("：")[1])
print(n_reviews)
