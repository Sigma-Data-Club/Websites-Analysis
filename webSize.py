from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests

# Replace 'website_domain' with the actual website domain you want to search
website_domain = 'n3xtsports.com'

# Set up the Selenium webdriver
driver = webdriver.Firefox()

# Open Google search
driver.get('https://www.google.com/search?q=site%3A'+website_domain)

# Button
search_button = driver.find_element(By.XPATH, '//*[@id="W0wltc"]')
search_button.click()

# Get the aproximate number of search results
search_results = driver.find_element(By.XPATH, '//*[@id="result-stats"]').text

search_results = search_results.split()[1]
search_results = int(search_results)

