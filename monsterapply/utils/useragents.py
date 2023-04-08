from time import sleep
from random import uniform

from typing import List, Dict

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def get_user_agent(operating_system: str = 'mac') -> str:

    software_names: List[Dict]= [SoftwareName.CHROME.value]
    operating_system: List[Dict] = [OperatingSystem.MAC.value]   

    match operating_system.lower():

        case 'windows': 
            operating_system = [OperatingSystem.WINDOWS.value]
        case 'linux':
            operating_system = [OperatingSystem.LINUX.value]
        case 'unix':
            operating_system = [OperatingSystem.UNIX.value]

    user_agent_rotator: UserAgent = UserAgent(software_names=software_names, 
                                              operating_systems=operating_system, 
                                              limit=15)
    
    return user_agent_rotator.get_random_user_agent()
