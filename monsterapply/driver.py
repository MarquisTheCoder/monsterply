

# driver dependency
import undetected_chromedriver as uc2

#selenium dependency
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options: Options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  
chrome_options.add_experimental_option("useAutomationExtension", False) 
chrome_options.add_argument("--disable-blink-features=AutomationControlled") 

chrome_options.add_argument(f'user-agent={BotAvoidance.return_mac_user_agent()}')


def get_driver():
    chrome: webdriver = uc2.Chrome(version_main=111, chrome_options=chrome_options)
    chrome.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 