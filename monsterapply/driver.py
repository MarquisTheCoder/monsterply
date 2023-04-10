


import undetected_chromedriver as uc2

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from utils.useragents import get_user_agent

from os import getlogin
import platform
import pickle

def new_driver() -> WebDriver:

    """Editing chrome options to avoid detection"""

    chrome_options: Options = Options()

    current_system: str = platform.system().lower()
        
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("useAutomationExtension", False) 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  

    chrome_options.add_argument(f'user-agent={get_user_agent()}')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") 

    chrome: WebDriver = uc2.Chrome(version_main=111, chrome_options=chrome_options)
    chrome.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

    if current_system == 'darwin':
        chrome_options.add_argument(f'user-data-dir=/Users/{getlogin()}/Library/Application Support/Google/Chrome/Default')

    elif current_system == 'windows':
        chrome_options.add_argument(f'user-data-dir=C:\Users\{getlogin()}\AppData\Local\Google\Chrome\User Data\Default')

    else:
        chrome_options.add_argument(f'user-data-dir=/home/{getlogin()}/. config/google-chrome/default')

    # cookies = pickle.load(open("cookies/cookies.pkl", "rb"))

    # for cookie in cookies:
    #     print(cookie)

    return chrome