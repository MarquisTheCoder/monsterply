


from random import choice, uniform
from time import sleep
from math import floor

from .wait import *


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def _calculate_type_speed(wpm: int) -> None:
    sleep(choice((uniform(70, 90), 
                   uniform(90,100), 
                   uniform(95,100))) 
                   / (wpm * uniform(3,4)))

def send(message: str, into: WebElement, driver: WebDriver) -> None:

    try:
        for character in message:
            into.send_keys(character)
            _calculate_type_speed
        randomize_pause(1,2.3)
        into.send_keys(Keys.ENTER)

    except Exception:
        pass
    
