from time import sleep
from random import uniform, normalvariate, randint, triangular, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def _calculate_type_speed(wpm: int) -> None:
    """Wait for a random amount of time to simulate human typing speed."""
    words_per_second = wpm / 60
    delay = normalvariate(1/words_per_second, 0.1) 
    sleep(delay)


def send(message: str, into: WebElement, driver: WebDriver, wpm: int = 200) -> None:
    """Type a message into an input field."""
    try:
        for i in range(len(message)):
            character = message[i]
            into.send_keys(character)
            _calculate_type_speed(wpm)
            if random() < 0.01:  
                _simulate_typing_error(into, message, i)
            if random() < 0.02:  
                pause_length = triangular(0.1, 0.5, 0.3)  
                sleep(pause_length)
            if random() < 0.02:  
                backspace_count = randint(1, 3)
                backspace_delay = uniform(0.5, 1.5)
                sleep(backspace_delay)
                for j in range(backspace_count):
                    into.send_keys(Keys.BACKSPACE)
                    sleep(uniform(0.1, 0.3))
                for j in range(backspace_count):
                    into.send_keys(message[i-j-1])
                    _calculate_type_speed(wpm)
        sleep(uniform(0.5, 1))  
        into.send_keys(Keys.RETURN)

    except Exception:
        pass


def _simulate_typing_error(into: WebElement, message: str, i: int, wpm: int = 100) -> None:
    """Simulate a typing error by backspacing and retyping the previous character."""
    sleep(uniform(0.1, 0.3))
    into.send_keys(Keys.BACKSPACE)
    sleep(uniform(0.1, 0.3))
    into.send_keys(message[i-1])
    _calculate_type_speed(2 * wpm) 