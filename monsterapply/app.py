
from traversing.paths.recommended_jobs import RecommendedPaths
from traversing.paths.home import HomePaths
from utils.useragents import get_user_agent
from factory import Factory
from cli import file


def main() -> None:
    # print(f'homepage -> home button = {HomePaths.home}')
    # print(f'recommended page -> home button = {RecommendedPaths.home}')
    # print(get_user_agent())
    # file()
    factory: Factory = Factory()
    factory.create_bot()


if __name__ == '__main__':
    main()