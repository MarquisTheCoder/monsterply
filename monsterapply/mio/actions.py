
from time import sleep
from random import uniform
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

# def move_pointer_to_element(element: WebElement, driver: WebDriver):
#     actions = ActionChains(driver)
#     actions.move_to_element(element).perform()

def move_pointer_to_element(element: WebElement, driver: WebDriver):
    ActionChains(driver)\
        .move_to_element(element)\
        .perform()

def scroll_within_element_y(element: WebElement, driver: WebDriver, y_scroll: int):
    ActionChains(driver)\
        .move_to_element(element)\
        .scroll_by_amount(0, y_scroll)\
        .perform()

        # get the x and y coordinates of the element
    # x, y = element.location["x"], element.location["y"]

    # # define a maximum distance to overshoot the element
    # max_overshoot = 40

    # # define the duration of the movement (in seconds)
    # duration = uniform(0.8, 1.2)

    # # calculate the maximum distance to overshoot based on the duration
    # max_overshoot_distance = max_overshoot * duration

    # # calculate the starting position of the movement
    # start_x = x + uniform(-max_overshoot_distance, max_overshoot_distance)
    # start_y = y + uniform(-max_overshoot_distance, max_overshoot_distance)

    # # create an ActionChains object and move the mouse cursor to the starting position
    # actions = ActionChains(driver)
    # actions.move_to_element_with_offset(element, start_x, start_y).perform()

    # # calculate the distance and direction to the element
    # dx = x - start_x
    # dy = y - start_y
    # distance = (dx ** 2 + dy ** 2) ** 0.5
    # direction = (dx / distance, dy / distance)

    # # define the step size (in pixels) and time interval (in seconds)
    # step_size = 10
    # time_interval = 0.01

    # # move the mouse cursor towards the element in steps
    # for i in range(int(distance / step_size)):
    #     # calculate the next position of the mouse cursor
    #     next_x = start_x + direction[0] * step_size * i
    #     next_y = start_y + direction[1] * step_size * i
        
    #     # add some variadic overshooting and corrections
    #     overshoot_distance = uniform(-max_overshoot_distance, max_overshoot_distance)
    #     overshoot_direction = (direction[1], -direction[0])
    #     next_x += overshoot_direction[0] * overshoot_distance
    #     next_y += overshoot_direction[1] * overshoot_distance
    #     next_x = max(min(next_x, x), start_x)
    #     next_y = max(min(next_y, y), start_y)
        
    #     # move the mouse cursor to the next position
    #     actions.move_to_element_with_offset(element, next_x, next_y).perform()
        
    #     # wait for a short time interval to simulate human-like movement
    #     sleep(time_interval)

    # # move the mouse cursor to the final position of the element
    # actions.move_to_element_with_offset(element, x, y).perform()

def open_new_tab(driver: WebDriver) -> None:
    driver.execute_script("window.open('');")
