

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
        self.search_job("Software Developer", "New York")
        self.load_jobs("Developer", "New York")

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


    def search_job(self, job: str, location: str) -> None:
        search_bar: WebElement = wait(HomePaths.search_bar, self.driver, timeout=180)
        send(job, into=search_bar, driver=self.driver)
        location_bar: WebElement = wait(HomePaths.location, self.driver)
        send(location, into=location_bar, driver=self.driver)
        wait(HomePaths.search_button, self.driver).click()

    def url_handling(self, url, next_page):
        x = url.split('&')
        for i in range(len(x) -1):
            if 'page' in x[i]:
                x.pop(i)
        return "&".join(x) + f'&page={next_page}'


    def check_page(self, base_url, next_page):

        parse_url = self.url_handling(base_url, next_page)

        response = requests.get(parse_url)
        if 'sorry' in response.text.lower():
            return False
        return True

    def load_jobs(self, search: str, location: str, current_page: int = 1) -> None: 

        hold: WebDriverWait = WebDriverWait(self.driver, 10000)

        self.driver.execute_script(f'window.scrollTo(0, {self.driver.get_window_size()["height"]})')

        hold.until(ec.presence_of_element_located((By.CLASS_NAME,"apply-buttonstyle__JobApplyButton-sc-1xcccr3-0")))

        self.driver.execute_script(f'window.scrollTo(0, {self.driver.get_window_size()["height"]})')

        randomize_pause(4,5)

        apply_buttons = self.driver.find_elements(By.CLASS_NAME, "apply-buttonstyle__JobApplyButton-sc-1xcccr3-0")

        for apply_button in apply_buttons:
            if 'quick' in apply_button.text.lower():
                print(apply_button.text)
                self.apply_for_job(apply_button)

        # next_page = f'https://{self.driver.current_url}jobs/search?q={search.replace(" ", "+")}&where={location}&page={current_page}' 
        # if self.check_page(next_page, current_page + 1):
        #     current_page = current_page + 1
        #     self.driver.get()
        #     self.load_jobs(current_page)  

    def apply_for_job(self, button: WebElement) -> None:
        button.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait('/html/body/div[1]/div[2]/div[2]/div/div/button', self.driver, timeout=30)
        randomize_pause(3,4.3)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    






    
