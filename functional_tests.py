import os
from selenium import webdriver

chromedriver = "/Users/Greg/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

#current_dir = os.getcwd()
#print(current_dir)

browser = webdriver.Chrome(chromedriver)

# Edith has heard about a cool new online todo app. She goes
# to check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list
# Edith wonders whether the site will remember her list. The she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Statisfied, she goes back to sleep

browser.quit()
