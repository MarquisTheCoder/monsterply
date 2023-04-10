

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import scipy.interpolate as si
from time import sleep
import numpy as np



def move_pointer_to_element(element: WebElement, driver: WebDriver):

   # Assume driver is a valid instance of a webdriver
# Assume element is the WebElement you want to move the mouse to

# Define the control points for the Bézier curve
    p0 = element.location
    p3 = element.location
    p1 = {'x': p0['x'] + 100, 'y': p0['y'] + 100}
    p2 = {'x': p3['x'] + 100, 'y': p3['y'] + 100}

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Calculate the position of the mouse pointer along the curve
    for t in range(0, 101, 5):
        x = ((1 - t / 100) ** 3) * p0['x'] + 3 * ((1 - t / 100) ** 2) * (t / 100) * p1['x'] + 3 * (1 - t / 100) * ((t / 100) ** 2) * p2['x'] + ((t / 100) ** 3) * p3['x']
        y = ((1 - t / 100) ** 3) * p0['y'] + 3 * ((1 - t / 100) ** 2) * (t / 100) * p1['y'] + 3 * (1 - t / 100) * ((t / 100) ** 2) * p2['y'] + ((t / 100) ** 3) * p3['y']

        # Move the mouse pointer to the calculated position
        actions.move_to_element_with_offset(element, x, y)

        # Perform the action
        actions.perform()

        # Wait for a short amount of time to simulate human-like movement
        sleep(0.1)
