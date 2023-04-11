

from mio.actions import *
# import mio.fields
# import mio.wait

from time import sleep
from datetime import datetime
from typing import TextIO, List

from driver import new_driver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from traversing.paths.types import XPATH
from traversing.paths.login import Login
from traversing.paths.home import HomePaths
from traversing.paths.recommended_jobs import RecommendedPaths


from mio.wait import *
from mio.actions import *
from mio.fields import send

"""Handles exception handling"""

from exceptions import *
import requests

base_url: str = "https://www.monster.com/"
google: str = "https://google.com"

class Crawler():

    driver: WebDriver = new_driver()
    
    def ___init__(self, 
                  hours: int = 2, 
                  run_at: datetime = None, 
                  run_until: datetime = None, 
                  jobs_raw: List[str] = None,
                  jobs_file: TextIO = None,
                  driver: WebDriver = driver,
                  current_page: int = 1) -> None:

        self.hours: int = hours
        self.run_at: datetime = run_at
        self.jobs_file: TextIO = jobs_file
        self.jobs_raw: List[str] = jobs_raw
        self.run_until: datetime = run_until
        self.driver: WebDriver = driver
        self.current_page = current_page  

    def crawl(self) -> None:
        self.goto_home()
        self.bypass_google_login()
        self.search_jobs("Web Developer", "Charlotte, NC", 1)


    def goto_home(self) -> None:
        self.driver.get(base_url)
    

    def open_login_page(self) -> None:
        login_button: WebElement = wait(HomePaths.login_button, self.driver)
        move_pointer_to_element(login_button, self.driver)
        randomize_pause(1, 2)
        login_button.click()


    def bypass_google_login(self) -> None: 
        original_window = self.driver.current_window_handle
        self.driver.switch_to.new_window('tab')
        self.driver.get(google)

    
        signed_in: WebElement = wait(Login.google.signed_in, 
                                         driver=self.driver,
                                         timeout=100)

        self.driver.close()
        self.driver.switch_to.window(original_window)
        
        homepage_login: WebElement = wait(HomePaths.login_button, driver=self.driver).click()
        randomize_pause(2,3)
        google_login: WebElement = wait(Login.google_login, driver=self.driver)
        google_login.click()


    def form_query(self, job: str, location: str, page: int):
        return f'https://www.monster.com/jobs/search?q={job}&where={location}&page={page}&so=m.h.lh' 
    

    def search_job(self, job: str, location: str, page: str) -> None:
        self.driver.get(self.form_query(job, location, page)) 
       

    def search_jobs(self, job: str, location: str, page: int ):

        takeaway_spaces: str = location.replace(" ", "+")
        takeaway_commas: str = takeaway_spaces.replace(",", "%2C")

        self.search_job(job, takeaway_commas, page)
        self.load_jobs(page)
        self.apply_for_jobs()
        self.check_next_page(job, location, page + 1)
        
    def check_next_page(self, job: str, location: str, page: int) -> bool:
        self.driver.get(self.form_query(job, location, page))
        randomize_pause(2,4)

        try:
            hold: WebDriverWait = WebDriverWait(self.driver, 5)
            hold.until(ec.presence_of_element_located((By.CLASS_NAME,"job-search-resultsstyle__JobCardWrap-sc-1wpt60k-5"))) 
            self.search_jobs(job, location, page)

        except Exception as e:
            print('last page found')
            exit(1)




    def load_jobs(self, current_page: int) -> None: 

        hold: WebDriverWait = WebDriverWait(self.driver, 10000)

        result_container: WebElement = hold.until(ec.presence_of_element_located((By.ID,"JobCardGrid")))

        window_height: float = self.driver.get_window_size()["height"] 
        offset: float = window_height / 10

        for page in range(current_page):

            scroll_within_element_y(driver=self.driver,
                                    element=result_container, 
                                    y_scroll=window_height + offset)

            randomize_pause(4,5)

    def apply_for_job(self, button: WebElement) -> None:
            button.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            wait('/html/body/div[1]/div[2]/div[2]/div/div/button', self.driver, timeout=30)
            randomize_pause(3,4.3)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def apply_for_jobs(self) -> None:

        apply_buttons = self.driver.find_elements(By.CLASS_NAME, "apply-buttonstyle__JobApplyButton-sc-1xcccr3-0")

        for apply_button in apply_buttons:
            if 'quick' in apply_button.text.lower():
                print(apply_button.text)
                self.apply_for_job(apply_button)

   

    






    
