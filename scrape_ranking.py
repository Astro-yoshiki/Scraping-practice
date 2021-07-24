import pandas as pd
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://scraping-for-beginner.herokuapp.com/ranking/"

data = []
for i in range(3):
    page = i + 1
    print(f"page: {page}")
    res = requests.get(BASE_URL + f"?page={page}")
    soup = BeautifulSoup(res.text, "html.parser")

    # firstly, let's scrape one data
    spots = soup.find_all("div", attrs={"class": "u_areaListRankingBox"})

    for spot in spots:
        # spot name
        spot_name = spot.find("div", attrs={"class": "u_title"})
        spot_name.find("span", attrs={"class": "badge"}).extract()
        name = spot_name.text.replace("\n", "")

        # spot evaluation
        eval_num = spot.find("div", attrs={"class": "u_rankBox"}).text

        # spot rate
        categoryItems = spot.find("div", attrs={"class": "u_categoryTipsItem"})
        categoryItems = categoryItems.find_all("dl")
        keys = []
        values = []
        for categoryItem in categoryItems:
            keys.append(categoryItem.dt.text)
            values.append(float(categoryItem.find("dd", attrs={"class": "is_rank"}).text))
        categoryItems = dict(zip(keys, values))

        details = categoryItems
        details["観光地名"] = name
        details["点数"] = float(eval_num)
        data.append(details)

# convert to csv file
df = pd.DataFrame(data)
df = df[['観光地名', '点数', '楽しさ', '人混みの多さ', '景色', 'アクセス']]  # switch columns
df.to_csv("ranking.csv", index=False)
