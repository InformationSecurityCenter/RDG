import requests
from checklib import Status


class Helper:
    TCP_CONNECTION_TIMEOUT = 15

    def __init__(self, checker, port: int = 5000):
        self.c = checker
        self.port = port
        self.base_url = f"http://{checker.host}:{port}"
        self.session = requests.Session()

    def register(self, username: str, password: str) -> requests.Response:
        url = f"{self.base_url}/register"
        payload = {'username': username, 'password': password, 'password2': password}
        response = self.session.post(url=url, data=payload)
        return response

    def login(self, username: str, password: str) -> requests.Response:
        url = f"{self.base_url}/login"
        payload = {'username': username, 'password': password}
        response = self.session.post(url, data=payload)
        return response

    def profile(self) -> requests.Response:
        url = f"{self.base_url}/profile"
        response = self.session.get(url)
        return response

    def create_flag(self, user_id: str, token: str, flag: str) -> requests.Response:
        url = f"{self.base_url}/api/users/{user_id}/flags"
        payload = {'flag': flag}
        headers = {'Authorization': f'Bearer {token}'}
        response = self.session.post(url, data=payload, headers=headers)
        return response

    def get_flag(self, user_id: str, flag_id: str, token: str) -> requests.Response:
        url = f"{self.base_url}/api/users/{user_id}/flags/{flag_id}"
        headers = {'Authorization': f'Bearer {token}'}
        response = self.session.get(url, headers=headers)
        return response

    def get_public_key(self):
        url = f"{self.base_url}/public_key"
        response = self.session.get(url)
        return response

    def get_user(self, user_id: str, token: str) -> requests.Response:
        url = f"{self.base_url}/api/users/{user_id}"
        headers = {'Authorization': f'Bearer {token}'}
        response = self.session.get(url, headers=headers)
        return response
