

from typing import Callable
from selenium.common.exceptions import NoSuchElementException


def raises_not_found(action) -> None:
    def check_script(*args, **kwargs):
        try:
            action(*args, **kwargs)
        except Exception:
            raise NoSuchElementException
            print("element not find")
    return check_script