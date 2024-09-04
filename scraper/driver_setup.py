import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--verbose")
    options.add_argument("--log-path=chromedriver.log")

    service = Service('/Users/ironman/Desktop/chromedriver-mac-arm64/chromedriver')

    driver = webdriver.Chrome(service=service, options=options)
    print("Chrome started successfully")
    
    return driver
