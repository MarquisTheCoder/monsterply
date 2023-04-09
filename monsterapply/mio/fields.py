


from random import choice
from time import sleep
from math import floor

from wait import wait
from ..traversing.paths.types import XPATH

from typing import Boolean 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


def _calculate_type_speed(wpm: int):
    return floor(choice([300, 400, 400, 500,600]) * 10 / wpm) 

def send(message: str, into: WebElement, driver: WebDriver) -> None:

    try:
        for character in message:
            into.send_keys(character)
            _calculate_type_speed(90)

        into.send_keys(Keys.ENTER)

    except Exception:
        pass
    
