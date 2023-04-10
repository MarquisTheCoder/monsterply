

from mio.actions import *
# import mio.fields
# import mio.wait

from time import sleep
from datetime import datetime
from typing import TextIO, List

from driver import new_driver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from traversing.paths.types import XPATH
from traversing.paths.login import Login
from traversing.paths.home import HomePaths
from traversing.paths.recommended_jobs import RecommendedPaths


from mio.wait import *
from mio.actions import *
from mio.fields import send

"""Handles exception handling"""

from exceptions import *


base_url: str = "https://www.monster.com/"
google: str = "https://accounts.google.com/v3/signin/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
class Crawler():

    driver = new_driver()

    def ___init__(self, 
                  hours: int = 2, 
                  run_at: datetime = None, 
                  run_until: datetime = None, 
                  jobs_raw: List[str] = None,
                  jobs_file: TextIO = None,
                  driver: WebDriver = driver) -> None:

        self.hours: int = hours
        self.run_at: datetime = run_at
        self.jobs_file: TextIO = jobs_file
        self.jobs_raw: List[str] = jobs_raw
        self.run_until: datetime = run_until
        self.driver: WebDriver = driver 


    def crawl(self) -> None:
        self.goto_home()
        # self.open_login_page()
        self.bypass_login()

    def goto_home(self) -> None:
        self.driver.get(base_url)
    
    def open_login_page(self) -> None:

        login_button: WebElement = wait(HomePaths.login_button, self.driver)
        move_pointer_to_element(login_button, self.driver)
        randomize_pause(1, 2)
        login_button.click()
        
    def bypass_login(self) -> None:

        open_new_tab(self.driver)

        self.driver.implicitly_wait(1)
        self.driver.switch_to(self.driver.window_handles[1])
        self.driver.get(google)

        email: WebElement = wait(Login.google.email, self.driver)
        send('deshawn.m.williams01@gmail.com', email, self.driver)
        randomize_pause(1,3)
        
        password: WebElement = wait(Login.google.password, self.driver)
        send('Ciddate0!', password, self.driver)
        randomize_pause(1,3)

        self.driver.implicitly_wait(1)

        self.driver.close()

        self.driver.switch_to(self.driver.window_handles[0])

    def search_job(self, job: str) -> None:
        search_bar: WebElement = wait(HomePaths.search_bar,self.driver, timeout=180)
        send(job, into=search_bar, driver=self.driver)



    
