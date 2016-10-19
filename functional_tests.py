import os
from selenium import webdriver

chromedriver = "/Users/Greg/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

#current_dir = os.getcwd()
#print(current_dir)

browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
