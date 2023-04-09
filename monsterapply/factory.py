

from datetime import datetime
from typing import TextIO

"""Will create bots here"""

class Factory:

    def ___init__(self, 
                  base_url: str, 
                  run_at: datetime, 
                  run_until: datetime, 
                  hours: 2, 
                  file: TextIO):

        self.base_url: str = base_url
        self.run_at: datetime = run_at
        self.run_until: datetime = run_until
        self.hours: int = hours
        self.file: TextIO = file

    def create_bot(self, driver):
        driver.get(self.base_url)
