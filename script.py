import requests
import pprint


URL = 'https://randomuser.me/api/'
PARAMS = {'results': 100,
          'gender': 'male'}


def get_contents(url: str) -> dict:
    """
    :param Entrypoint to REST API
    :return: Dictionary of random user data
    """
    tmp = requests.get(url=url, params=PARAMS).json()
    results = tmp['results']
    return results


def main():
    content = get_contents(URL)
    # pprint.pprint(content)
    return content


if __name__ == '__main__':
    main()