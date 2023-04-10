

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from driver import new_driver
from mio.wait import wait
from traversing.paths.home import HomePaths


import pickle
import asyncio
from time import sleep
from itertools import count
from concurrent.futures import ProcessPoolExecutor

driver: WebDriver = new_driver()

executor = ProcessPoolExecutor(2)
loop = asyncio.new_event_loop()
baa = loop.run_in_executor(executor, save_cookies)

loop.run_forever()

def start_driver():
    driver.get("https://google.com")
    wait(HomePaths.home, driver=driver, timeout=100000)


def save_cookies():
    for _ in count(0):
        sleep(0.5)
        pickle.dump(driver.get_cookies(), open("cookies/cookies.pkl", "wb"))

start_driver()
