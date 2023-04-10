

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

driver: WebDriver = new_driver()

async def start_driver():
    driver.get("https://google.com")
    await sleep(2)
    wait(HomePaths.home, driver=driver, timeout=100000)


async def save_cookies():
    async for _ in count(0):
        sleep(0.5)
        pickle.dump(driver.get_cookies(), open("cookies/cookies.pkl", "wb"))


async def run_both():
    start_driver()
    save_cookies()


asyncio.run(run_both())