
import sys
sys.path.append('../../..')
from ... types import XPATH 

class RecommendedPaths:
    home: XPATH = '/html/body/div[1]/header/div[3]/div/div[2]/a'
    searchbar: XPATH = '//*[@id="horizontal-input-one-undefined"]'
    search_button: XPATH = '/html/body/div[1]/header/div[3]/div/div[3]/div/div/form/div/button[2]'
    search_location: XPATH = '//*[@id="horizontal-input-two-undefined"]'
    