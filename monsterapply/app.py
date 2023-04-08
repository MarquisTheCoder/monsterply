
from traversing.paths.recommended_jobs import RecommendedPaths
from traversing.paths.home import HomePaths


def main():
    print(f'homepage -> home button = {HomePaths.home}')
    print(f'recommended page -> home button = {RecommendedPaths.home}')

if __name__ == '__main__':
    main()