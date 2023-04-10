

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from driver import new_driver

driver: WebDriver = new_driver()
driver.get("https://google.com")
