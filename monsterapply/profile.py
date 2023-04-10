

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from driver import new_driver
from mio.wait import wait
from traversing.paths.home import HomePaths
driver: WebDriver = new_driver()
driver.get("https://google.com")
wait(HomePaths.home, driver=driver, timeout=100000)
