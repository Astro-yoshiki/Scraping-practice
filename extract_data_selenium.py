from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options
options = Options()
options.add_argument("--headless")

URL = "https://scraping-for-beginner.herokuapp.com/login_page"
browser = webdriver.Chrome(options=options)  # /usr/local/bin/
browser.get(URL)

browser.find_element_by_id("username").send_keys("imanishi")
browser.find_element_by_id("password").send_keys("kohei")
browser.find_element_by_id("login-btn").click()

# scraping from web page
# extract one by one
name = browser.find_element_by_id("name").text
company = browser.find_element_by_id("company").text
birthday = browser.find_element_by_id("birthday").text
come_from = browser.find_element_by_id("come_from").text
hobby = browser.find_element_by_id("hobby").text.replace("\n", ",")
# print(name, company, birthday, come_from, hobby)

# extract whole element(s)
elems_th = browser.find_elements_by_tag_name("th")
keys = []
for elem_th in elems_th:
    keys.append(elem_th.text)

elems_td = browser.find_elements_by_tag_name("td")
values = []
for elem_td in elems_td:
    values.append(elem_td.text)

for key, value in zip(keys, values):
    print(f"{key}: {value} \n")

browser.quit()
