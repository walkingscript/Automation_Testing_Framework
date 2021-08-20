import requests


class Request:

    @staticmethod
    def basic_auth(url, username, password) -> str:
        url = url.replace('//', f'//{username}:{password}@', 1)
        data = requests.get(url)
        return data.json()
