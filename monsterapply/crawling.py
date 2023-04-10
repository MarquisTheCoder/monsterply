

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
from mio.fields import send
from mio.actions import move_pointer_to_element

"""Handles exception handling"""

from exceptions import *


base_url: str = "https://www.monster.com/"

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
        self.open_login_page()
        self.bypass_login('deshawn.m.williams01@gmail.com', 'Ciddate0!')

    def goto_home(self) -> None:
        self.driver.get(base_url)
    
    def open_login_page(self) -> None:

        login_button: WebElement = wait(HomePaths.login_button, self.driver)
        move_pointer_to_element(login_button, self.driver)
        login_button.click()

        """logged in already"""

    def bypass_login(self, email: str, password: str) -> None:

        login_with_google: WebElement = wait(Login.google_login, self.driver)
        move_pointer_to_element(login_with_google, self.driver)
        login_with_google.click()
        
        randomize_pause(1.0, 2.5)

        google_login_email: WebElement = wait(Login.google.email, self.driver)
        move_pointer_to_element(google_login_email, self.driver)
        send(email, into=google_login_email, driver=self.driver)

        randomize_pause(1.0, 2.5)
        
        google_login_email_next: WebElement = wait(Login.google.next_email, self.driver)
        move_pointer_to_element(google_login_email_next, self.driver)
        google_login_email_next.click()

        randomize_pause(0.5, 3.2)

        google_login_password: WebElement = wait(Login.google.password, self.driver)
        move_pointer_to_element(google_login_password, self.driver)
        send(password, into=google_login_password, driver=self.driver)

        randomize_pause(1.2, 4.0)

        google_login_password_next: WebElement = wait(Login.google.next_password, self.driver)
        move_pointer_to_element(google_login_email_next, self.driver)
        google_login_password_next.click()
 
    # @raises_not_found
    def search_job(self, job: str) -> None:
        search_bar: WebElement = wait(HomePaths.search_bar,self.driver, timeout=180)
        send(job, into=search_bar, driver=self.driver)



    
