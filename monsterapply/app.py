
from traversing.paths.recommended_jobs import RecommendedPaths
from traversing.paths.home import HomePaths
from utils.useragents import get_user_agent
from cli import file

from driver import new_driver
from crawling import Crawler

def main() -> None:
    print(f'homepage -> home button = {HomePaths.home}')
    print(f'recommended page -> home button = {RecommendedPaths.home}')
    print(get_user_agent())
    # file()

    crawler: Crawler = Crawler()
    crawler.crawl()
    
if __name__ == '__main__':
    main()