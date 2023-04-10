


from random import choice
from time import sleep
from math import floor

from .wait import *


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def _calculate_type_speed(wpm: int):
    return floor(choice((50, 100, 100, 150)) / (wpm * 1.5)) 

def send(message: str, into: WebElement, driver: WebDriver) -> None:

    try:
        for character in message:
            into.send_keys(character)
            sleep(_calculate_type_speed(40))

        randomize_pause(1,2.3)
        into.send_keys(Keys.ENTER)

    except Exception:
        pass
    
