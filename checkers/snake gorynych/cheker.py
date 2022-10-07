#!/usr/bin/env python3

import sys


from typing import Tuple, Optional
from requests import Response
from requests.exceptions import ConnectionError

from lib import Helper
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

        creds = self.helper.get_creds()
        username = creds[0]
        password = creds[1]
        response: Response = self.helper.login(username, password) #проверка входа
        if not 'Данные пользователей виртуального хостинга' in response.text:
            self.cquit(Status.MUMBLE, "Login failed", "Invalid username or password for operator user or login broken")

        response: Response = self.helper.check_work_of_cookie() #проверка что куки работают
        if not 'login.php' in response.text:
            self.cquit(Status.MUMBLE, "auth without cookie", "Check of cookie dont work, free auth")


        response: Response = self.helper.check_site1()
        if not 'Сайт с котиками' in response.text:
            self.cquit(Status.MUMBLE, "site1 (cats) dont work", "site1 (cats) dont work, port 1001")


        response: Response = self.helper.check_site2()
        if not 'Гороскоп' in response.text:
            self.cquit(Status.MUMBLE, "site2 (astr) dont work", "site2 (astr) dont work, port 1002")

        response: Response = self.helper.check_site3()
        if not 'Hackers' in response.text:
            self.cquit(Status.MUMBLE, "site3 (hackers) dont work", "site3 (hackers) dont work, port 1003")


        Response = self.helper.check_ssh_connect()
        if 'Permission denied, please try again' in Response:
            self.cquit(Status.MUMBLE, "sshpass cant login", "wrong password")
    
        self.cquit(Status.OK)



    def put(self, flag_id: str, flag: str, vuln: str):
        creds = self.helper.get_creds()
        username = creds[0]
        password = creds[1]
        if vuln == "1":
            response: Response = self.helper.login(username, password) #проверка входа
            if not 'Данные пользователей виртуального хостинга' in response.text:
                self.cquit(Status.MUMBLE, "Login failed", "Invalid creds for operator user or auth broken")

            response: Response = self.helper.create_flag_vuln1(flag) #устанавливаем флаг
            if response.status_code not in [200, 201]:
                self.cquit(Status.MUMBLE, "Failed create a new flag", response.text)

            response: Response = self.helper.get_flag_vuln1(flag) #проверяем установленный флаг
            if response.status_code != 200:
                self.cquit(Status.MUMBLE, "Failed to connect apache2 after PUT", response.text)

            if not flag in response.text:
                self.cquit(Status.MUMBLE, "Failed to get flag from response after PUT", "The flag is missing")


        if vuln == "2":
            response2 = self.helper.create_flag_vuln2(flag) #устанавливаем флаг
            if 'Permission denied' in response2:
                self.cquit(Status.MUMBLE, "SSH Login failed", "Invalid username or password for operator")
            #print(response2)

            check_put = self.helper.get_flag_vuln2(flag)
            if not flag in check_put:  #проверяем установленный флаг
                self.cquit(Status.MUMBLE, "Failed to get flag from SHH put", "The flag is missing")

        self.cquit(Status.OK)


    def get(self, flag_id: str, flag: str, vuln: str):
        
        if vuln == "1":
            creds = self.helper.get_creds()
            username = creds[0]
            password = creds[1]

            response: Response = self.helper.login(username, password)

            response: Response = self.helper.get_flag_vuln1(flag)
            if response.status_code != 200:
                self.cquit(Status.MUMBLE, "Failed to get existing flag", response.text)
            #print(response.text)
            if not flag in response.text:
                self.cquit(Status.MUMBLE, "Failed to get flag from response", "The flag is missing on the page ")

        if vuln == "2":
            response2 = ""
            response2 = self.helper.get_flag_vuln2(flag)
            #print("asdasd" + response2)

            if not flag in response2:
                self.cquit(Status.MUMBLE, "Failed to get flag from response ssh", "The flag is missing")

        self.cquit(status.Status.OK)


if __name__ == '__main__':
    c = Checker(sys.argv[2])
    try:
        c.action(sys.argv[1], *sys.argv[3:])
    except c.get_check_finished_exception() as e:
        cquit(Status(c.status), c.public, c.private)