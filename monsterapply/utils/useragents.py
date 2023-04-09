
from typing import List, Dict
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def get_user_agent(operating_system: str = 'mac') -> str:

    software_names: List[Dict]= [SoftwareName.CHROME.value]

    operating_systems: List[Dict] = [OperatingSystem.MAC.value]   

    if(operating_system.lower() == 'windows'):
        operating_systems = [OperatingSystem.WINDOWS.value]
    elif(operating_system.lower() == 'linux'):
        operating_systems = [OperatingSystem.LINUX.value]
    elif(operating_system.lower() == 'unix') :
        operating_systems = [OperatingSystem.UNIX.value]

    user_agent_rotator: UserAgent = UserAgent(software_names=software_names, 
                                              operating_systems=operating_systems, 
                                              limit=15)
    
    return user_agent_rotator.get_random_user_agent()
