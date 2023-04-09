

from .io.wait import wait
from .io.fields import fields
from .io.actions import *

from time import sleep
from datetime import datetime
from typing import TextIO, List

from driver import new_driver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from .traversing.paths.types import XPATH
from .traversing.paths.home import HomePaths
from .traversing.paths.recommended_jobs import RecommendedPaths

"""Handles exception handling"""

from .exceptions import *


base_url: str = "https://www.monster.com/"

class Crawling:

    def ___init__(self, 
                  hours: int = 2, 
                  run_at: datetime = None, 
                  run_until: datetime = None, 
                  jobs_raw: List[str] = None,
                  jobs_file: TextIO = None) -> None:

        self.hours: int = hours
        self.run_at: datetime = run_at
        self.jobs_file: TextIO = jobs_file
        self.jobs_raw: List[str] = jobs_raw
        self.run_until: datetime = run_until
        self.driver: WebDriver = new_driver()


    def crawl(self):
        self.goto_home()
        self.open_login_page()
        self.search_job("Python Developer")

    def goto_home(self):
        self.driver.get(base_url)
    
    def open_login_page(self):
        try:

            login_button: WebElement = wait(HomePaths.login_button, self.driver)
            move_pointer_to_element(self.driver, login_button)
            login_button.click()
            sleep(5000)
            
        except Exception:
            """logged in already"""

    @raises_not_found
    def search_job(self, job: str):
        search_bar: WebElement = wait(HomePaths.search_bar)
        fields.send(job, into=search_bar, driver=self.driver)



    
