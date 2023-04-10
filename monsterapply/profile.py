

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from driver import new_driver
from mio.wait import wait
from traversing.paths.home import HomePaths


import pickle
import asyncio
from time import sleep

driver: WebDriver = new_driver()

def start_driver():
    driver.get("https://google.com")
    wait(HomePaths.home, driver=driver, timeout=100000)
    pickle.dump(driver.get_cookies(), open("cookies/cookies.pkl", "wb"))

start_driver()
