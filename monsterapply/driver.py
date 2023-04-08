


import undetected_chromedriver as uc2

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from utils.useragents import get_user_agent

chrome_options: Options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  
chrome_options.add_experimental_option("useAutomationExtension", False) 
chrome_options.add_argument("--disable-blink-features=AutomationControlled") 

chrome_options.add_argument(f'user-agent={get_user_agent()}')

def get_driver() -> WebDriver:
    chrome: WebDriver = uc2.Chrome(version_main=111, chrome_options=chrome_options)
    chrome.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    return chrome