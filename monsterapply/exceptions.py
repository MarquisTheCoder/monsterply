

from typing import Callable
from selenium.common.exceptions import NoSuchElementException


def raises_not_found(action) -> None:
    def check_script(*args, **kwargs):
        try:
            action(*args, **kwargs)
        except NoSuchElementException(Exception):
            Exception.with_traceback()
    return check_script