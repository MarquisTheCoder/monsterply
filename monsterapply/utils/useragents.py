from time import sleep
from random import uniform

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.CHROME.value]

operating_systems = [OperatingSystem.MAC.value]   
    
user_agent_rotator = UserAgent(software_names=software_names, 
                                operating_systems=operating_systems, 
                                limit=100)

def return_mac_user_agent():
    return user_agent_rotator.get_user_agents()
