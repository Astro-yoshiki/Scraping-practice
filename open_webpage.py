from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options
options = Options()
options.add_argument("--headless")

# open web page
URL = "https://scraping-for-beginner.herokuapp.com/login_page"
browser = webdriver.Chrome(options=options)  # /usr/local/bin/
sleep(1)
browser.get(URL)

# log in(1. get tag 2. concrete operation)
# get tag
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
login_btn = browser.find_element_by_id("login-btn")

# concrete operation
username.send_keys("imanishi")
password.send_keys("kohei")
login_btn.click()

# quite browser
browser.quit()
