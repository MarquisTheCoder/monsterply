

from wait import wait
from ..traversing.paths.types import XPATH

from typing import Boolean 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

import random

def _read(message: str):
    pass

def send(message: str, into: XPATH, driver: WebDriver) -> None:
    try:
        field: WebElement = wait(to_find=into, driver=driver)
        
    except Exception:
        pass
    
