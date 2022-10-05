#!/usr/local/bin/python3.9
import sys

import jwt
from typing import Tuple, Optional
from requests import Response
from requests.exceptions import ConnectionError

from helper import Helper
from checklib import status, BaseChecker, generators, Status, cquit


class Checker(BaseChecker):
    vulns: int = 2
    timeout: int = 15
    uses_attack_data: bool = True

    def __init__(self, *args, **kwargs):
        super(Checker, self).__init__(*args, **kwargs)
        self.helper = Helper(self)

    def action(self, action, *args, **kwargs):
        try:
            super(Checker, self).action(action, *args, **kwargs)
        except ConnectionError as err:
            self.cquit(Status.DOWN, 'Connection error', f'Got requests connection error, err: {err}')

    def check(self):
        username = generators.rnd_username(5)
        password = generators.rnd_password(10)

        response: Response = self.helper.register(username, password)
        if 'Congratulations, you are now a registered user!' not in response.text:
            self.cquit(Status.MUMBLE, "Register failed", f"Register failed: {response.text}")

        if 'Please use a different username.' in response.text:
            self.cquit(Status.MUMBLE, "Register failed", "Such user already exist")

        response: Response = self.helper.login(username, password)
        if 'Invalid username or password' in response.text:
            self.cquit(Status.MUMBLE, "Login failed", "Invalid username or password for new user")

        token = response.cookies.get('access_token')
        if token is None:
            self.cquit(Status.MUMBLE, "Failed to get access token", "Cookie 'access_token' is empty")

        claims = jwt.decode(token, options={"verify_signature": False})
        user_id = claims.get('id')
        if user_id is None:
            self.cquit(Status.MUMBLE, "Token mismatch", "Failed to get 'id' attr from claims")

        response: Response = self.helper.get_user(user_id, token)
        if response.status_code != 200:
            self.cquit(Status.MUMBLE, "API: Failed to get user", response.text)

        data = response.json()
        if data.get('username') != username:
            self.cquit(Status.MUMBLE, "API: Usernames mismatch", response.text)

        response: Response = self.helper.profile()
        if 'Profile' not in response.text:
            self.cquit(Status.MUMBLE, "Profile failed", "Failed to check profile")

        response: Response = self.helper.get_public_key()
        if not response.text.startswith('ssh-ed25519'):
            self.cquit(Status.MUMBLE, "Public key failed", "Failed to get public key")

        self.cquit(Status.OK)

    def put(self, flag_id: str, flag: str, vuln: str):
        username = generators.rnd_username(5)
        password = generators.rnd_password(10)

        self.helper.register(username, password)
        response: Response = self.helper.login(username, password)

        token = response.cookies.get('access_token')
        if token is None:
            self.cquit(Status.MUMBLE, "Failed to get access token", "Cookie 'access_token' is empty")

        claims = jwt.decode(token, options={"verify_signature": False})
        user_id = claims.get('id')
        if user_id is None:
            self.cquit(Status.MUMBLE, "Token mismatch", "Failed to get 'id' attr from claims")

        response: Response = self.helper.create_flag(user_id, token, flag)
        if response.status_code not in [200, 201]:
            self.cquit(Status.MUMBLE, "Failed create a new flag", response.text)

        data = response.json()
        internal_flag_id = data.get('id')
        if internal_flag_id is None:
            self.cquit(Status.MUMBLE, "Failed to get flag id from response", response.text)

        self.cquit(status.Status.OK, username, f'{username}*{user_id}*{internal_flag_id}*{token}')

    def get(self, flag_id: str, flag: str, vuln: str):
        _, user_id, flag_id, token = flag_id.split('*')

        response: Response = self.helper.get_flag(user_id, flag_id, token)
        if response.status_code != 200:
            self.cquit(Status.MUMBLE, "Failed to get existing flag", response.text)

        data = response.json()
        if data.get('flag') is None:
            self.cquit(Status.MUMBLE, "Failed to get flag id from response", response.text)

        if data.get('flag') != flag:
            self.cquit(Status.CORRUPT, "Flags not eq", response.text)

        self.cquit(status.Status.OK)


if __name__ == '__main__':
    c = Checker(sys.argv[2])

    try:
        c.action(sys.argv[1], *sys.argv[3:])
    except c.get_check_finished_exception() as e:
        cquit(Status(c.status), c.public, c.private)
