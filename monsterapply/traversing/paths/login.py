from .types import XPATH

class Login:
    google_login: XPATH = '//*[@id="__next"]/div[2]/div/div[3]/div/div/main/form/div[3]/div[3]/button'
    facebook_login: XPATH = '//*[@id="__next"]/div[2]/div/div[3]/div/div/main/form/div[3]/div[2]/button'
    apple_login: XPATH = '//*[@id="__next"]/div[2]/div/div[3]/div/div/main/form/div[3]/div[1]/button'
    email: XPATH = '//*[@id="email"]'
    password: XPATH = '//*[@id="password"]'

    class google:
        email: XPATH = '//*[@id="identifierId"]'
        