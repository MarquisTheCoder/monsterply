

from datetime import datetime
from typing import TextIO

from driver import new_driver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

"""Will create bots here"""

class Factory:

    base_url: str = "https://www.monster.com/"

    def ___init__(self, 
                  run_at: datetime = None, 
                  run_until: datetime = None, 
                  hours: int = 2, 
                  file: TextIO = None):

        self.run_at: datetime = run_at
        self.run_until: datetime = run_until
        self.hours: int = hours
        self.file: TextIO = file
        self.driver: WebDriver = new_driver()

    def create_bot(self):
        self.driver.get(Factory.base_url)
