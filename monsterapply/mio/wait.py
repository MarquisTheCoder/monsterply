

from time import sleep
from random import uniform

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec


from selenium.common.exceptions import NoSuchElementException

def mili_to_seconds(mili: int) -> int:
    return mili * 1_000

def wait(to_find: str, driver: WebDriver,timeout: int = mili_to_seconds(15)):

    timeout = mili_to_seconds(timeout)
    wait: WebDriverWait = WebDriverWait(driver, timeout)

    # try:
    to_find: WebElement = wait.until(ec.presence_of_element_located((By.XPATH, to_find)))
    return to_find
    
    # except Exception:
    #    raise NoSuchElementException

def randomize_pause_for(method, start: float, end: float) -> None:
    def page_action(*args, **kwargs):
        sleep(uniform(start,end))
        method(*args, **kwargs)
    return page_action

def randomize_pause(start: float, end: float) -> None:
    sleep(uniform(start, end))
