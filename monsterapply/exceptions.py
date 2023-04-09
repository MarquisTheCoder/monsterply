

from typing import Callable
from selenium.common.exceptions import NoSuchElementException


def raises_not_found(action: Callable(...)) -> None:
    try:
        action()
    except NoSuchElementException(Exception):
        print(Exception.with_traceback)
