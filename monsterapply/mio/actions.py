

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import scipy.interpolate as si
import numpy as np



def move_pointer_to_element(element: WebElement, driver: WebDriver):

    # B-Line Curve base:
    points = [[0, 0], [0, 2], [2, 3], [4, 0], [6, 3], [8, 2], [8, 0]];
    points = np.array(points)

    x = points[:,0]
    y = points[:,1]


    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)

    x_tup = si.splrep(t, x, k=3)
    y_tup = si.splrep(t, y, k=3)

    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

    x_i = si.splev(ipl_t, x_list) # x interpolate values
    y_i = si.splev(ipl_t, y_list) # y interpolate values

    action = ActionChains(driver)
    
    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_to_element_by_offset(element, mouse_x, mouse_y);
        action.perform();
        print(mouse_x, mouse_y)
