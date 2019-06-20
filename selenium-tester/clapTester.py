import sys
import os
from selenium import webdriver
browser = webdriver.Chrome(executable_path=r"/Users/angelogiacco/Documents/GitHub/mediumBooster/selenium-tester/chromedriver")
browser.get('https://medium.com/ahmed-t-ali/lets-build-a-github-pro-bot-5e155cec395f')
clap_button = browser.find_elements_by_xpath('//*[@id="_obv.shell._surface_1561035526164"]/div/main/article/footer/div[1]/div[3]/div/div[1]/div/div/button')[0]
for i in range(10):
    clap_button.click()
