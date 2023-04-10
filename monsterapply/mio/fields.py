

import random
from time import sleep
from math import floor

from .wait import *


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def _calculate_type_speed(wpm: int) -> None:
    words_per_second = wpm / 60
    delay = random.expovariate(words_per_second)  # use exponential distribution for natural typing rhythm
    sleep(delay)

def send(message: str, into: WebElement, driver: WebDriver, wpm: int = 120) -> None:
    """Type a message into an input field."""
    try:
        for character in message:
            into.send_keys(character)
            _calculate_type_speed(wpm)
            if random.random() < 0.1:
                backspace_count = random.randint(1, 3)
                backspace_delay = random.uniform(0.5, 1.5)
                sleep(backspace_delay)
                for i in range(backspace_count):
                    into.send_keys(Keys.BACKSPACE)
                    sleep(random.uniform(0.1, 0.3))
                for i in range(backspace_count):
                    into.send_keys(message[-i-1])
                    _calculate_type_speed(wpm)
        sleep(random.uniform(0.5, 1))
        into.send_keys(Keys.RETURN)

    except Exception:
        pass