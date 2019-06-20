import sys
import os
from selenium import webdriver
browser = webdriver.Chrome(executable_path=r"/Users/angelogiacco/Documents/GitHub/mediumBooster/selenium-tester/chromedriver")
browser.get('https://medium.com/ahmed-t-ali/lets-build-a-github-pro-bot-5e155cec395f')
clap_button = browser.find_element_by_class_name('clapButton')
for i in range(10):
    clap_button.click()
