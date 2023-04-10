from .types import XPATH

class Login:
    google_login: XPATH = '/html/body/div[1]/div/div[2]/div/div[3]/div/div/main/form/div[3]/div[3]/button'
    facebook_login: XPATH = '//*[@id="__next"]/div[2]/div/div[3]/div/div/main/form/div[3]/div[2]/button'
    apple_login: XPATH = '//*[@id="__next"]/div[2]/div/div[3]/div/div/main/form/div[3]/div[1]/button'
    email: XPATH = '//*[@id="email"]'
    password: XPATH = '//*[@id="password"]'

    class google:
        email: XPATH = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
        next_email: XPATH = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button' 
        password: XPATH = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
        next_password: XPATH = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button'
        signed_in: XPATH = '/html/body/div[3]/header/div[2]/div[1]/div[4]/div/a'
