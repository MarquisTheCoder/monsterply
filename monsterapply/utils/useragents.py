from time import sleep
from random import uniform

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.CHROME.value]

operating_system = [OperatingSystem.MAC.value]   
    


def get_user_agent(operating_system = 'mac'):

    match operating_system.lower():
        case 'windows': 
            operating_system = [OperatingSystem.WINDOWS.value]
        case 'linux':
            operating_system = [OperatingSystem.LINUX.value]
        case 'unix':
            operating_system = [OperatingSystem.UNIX.value]

    user_agent_rotator = UserAgent(software_names=software_names, 
                                operating_systems=operating_system, 
                                limit=100)
    
    return user_agent_rotator.get_user_agents()
