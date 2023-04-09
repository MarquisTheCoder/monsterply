
from .types import XPATH

class HomePaths:
    home: XPATH = '/html/body/div[1]/div[1]/header/div[4]/div/div[2]/a'
    search_bar: XPATH = '//*[@id="horizontal-input-one-undefined"]'
    search_button: XPATH = '/html/body/div[1]/div[1]/main/section[1]/div/div/div/div[1]/div/span/div/div/div[1]/form/div/button[2]'
    search_location: XPATH = '//*[@id="horizontal-input-two-undefined"]'
    view_all_button: XPATH = '/html/body/div[1]/div[1]/main/section[2]/div/div/div/div[1]/a'
    login_button: XPATH = '/html/body/div[1]/div[1]/header/div[4]/div/div[4]/div/a[2]'
