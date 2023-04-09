

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

def move_pointer_to_element(driver: WebDriver,element: WebElement):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()