

from wait import wait
from ..traversing.paths.types import XPATH

from typing import Boolean 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from time import sleep
from random import choice
from math import floor

def calculate_type_speed(wpm: int):
    return floor(choice([300, 400, 400, 500,600]) * 10 / wpm) 

def send(message: str, into: XPATH, driver: WebDriver) -> None:

    try:
        field: WebElement = wait(to_find=into, driver=driver)

        for character in message:
            field.send_keys(character)
            calculate_type_speed(90)

        field.send_keys(Keys.ENTER)
        
    except Exception:
        pass
    
