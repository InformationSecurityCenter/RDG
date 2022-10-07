import requests
from checklib import Status
from random import randint
import subprocess
import os
from checklib import status, BaseChecker, generators, Status, cquit
class Helper:
    TCP_CONNECTION_TIMEOUT = 15

    def __init__(self, checker, port: int = 1000):
        self.c = checker
        self.port = port
        self.host = checker.host
        self.base_url_no_port = f"http://{checker.host}"
        self.base_url = f"http://{checker.host}:{port}"
        self.session = requests.Session()

    def register(self, username: str, password: str) -> requests.Response:
        url = f"{self.base_url}/register"
        payload = {'username': username, 'password': password, 'password2': password}
        response = self.session.post(url=url, data=payload)
        return response

    def get_creds(self):
        print(self.host)
        host_ip=self.host
        print(host_ip)
        if (host_ip == "10.20.1.5"):
            creds = ['0t_v1nt4', 'atdf2022sdkinf3812ds']
        if (host_ip == "10.20.2.5"):
            creds = ['5599002010931470', 'atdf2022jidbf139f1j1jd']
        if (host_ip == "10.20.3.5"):
            creds = ['b_b', 'atdf2022hwrhn42h2h2']
        if (host_ip == "10.20.4.5"):
            creds = ['crescent', 'atdf2022j9812fh1ung10']
        if (host_ip == "10.20.5.5"):
            creds = ['menofhonestdestiny', 'atdf2022sdj9j1f81ndgkia']
        if (host_ip == "10.20.6.5"):
            creds = ['zavod', 'atdf2022asfggqgqwegq']
        if (host_ip == "10.20.7.5"):
            creds = ['inception', 'atdf2022dkd9iq8bhfq']
        if (host_ip == "10.20.8.5"):
            creds = ['thereisnoinforoma', 'atdf2022aklsd92fj1f1g']    
        if (host_ip == "10.20.9.5"):
            creds = ['return0', 'atdf2022sk9fj1ngg1gasf']
        if (host_ip == "10.20.10.5"):
            creds = ['themightynine', 'atdf2022sfnio1qnf912fb']
        return creds

    def login(self, username: str, password: str) -> requests.Response:
        url = f"{self.base_url}/login.php"

        payload = {'login': username, 'password': password}
        response = self.session.post(url, data=payload)
        return response

    def check_work_of_cookie(self):
        url = f"{self.base_url}/admin_panel/sites.html"
        res = requests.post(url)
        return res

    def check_site1(self):
        url = f"{self.base_url_no_port}:1001/"
        res = requests.post(url)
        return res

    def check_site2(self):
        url = f"{self.base_url_no_port}:1002/"
        res = requests.post(url)
        return res

    def check_site3(self):
        url = f"{self.base_url_no_port}:1003/"
        res = requests.post(url)
        return res


    def create_flag_vuln1(self, flag: str) -> requests.Response:
        url = f"{self.base_url}/admin_panel/users/add_new_user.php"

        names = ['Абрамов Марк Никитич', 'Аксенова Екатерина Максимовна', 'Аксенова Полина Александровна', 'Александров Дмитрий Фёдорович',
                 'Алексеева Владислава Тимофеевна', 'Алексеева Арина Ивановна', 'Андреева Мария Матвеевна', 'Андреева Вера Андреевна',
                 'Андреева Алиса Ярославовна', 'Андрианов Лев Артёмович', 'Баженова Виктория Александровна', 'Белкина Юлия Данииловна',
                 'Белоусова Ирина Всеволодовна', 'Беляев Даниил Никитич', 'Беляев Григорий Дмитриевич', 'Беляева София Ильинична', 'Белякова Вероника Романовна',
                 'Беспалов Тимур Михайлович', 'Беспалова Виктория Александровна', 'Бобров Егор Павлович', 'Богомолова Арина Егоровна', 'Богомолова Анна Петровна',
                 'Борисов Вадим Максимович', 'Борисова Мия Викторовна', 'Бородин Кирилл Кириллович', 'Быков Тимофей Макарович', 'Васильев Артём Александрович',
                 'Васильев Кирилл Германович', 'Васильева Виктория Сергеевна', 'Виноградова Валерия Борисовна', 'Власова Арина Леоновна', 'Волкова Ева Макаровна',
                 'Воробьев Михаил Матвеевич', 'Воробьева Александра Константиновна', 'Воробьева Арина Ярославовна', 'Воробьева Валерия Матвеевна', 'Гаврилов Дмитрий Глебович',
                 'Гаврилов Роман Кириллович', 'Гаврилова Мария Фёдоровна', 'Герасимова Василиса Викторовна', 'Гладков Лев Артёмович', 'Головин Захар Артёмович',
                 'Голубева Валерия Львовна', 'Гончаров Дмитрий Артемьевич', 'Гончаров Константин Николаевич', 'Гончарова Алиса Серафимовна', 'Горбунов Артём Максимович',
                 'Горбунова Виктория Ярославовна', 'Горбунова Анна Семёновна', 'Громова Алиса Дмитриевна', 'Гусев Артём Сергеевич', 'Гусева Виктория Артёмовна',
                 'Давыдова Анна Александровна', 'Данилова Варвара Ивановна', 'Дементьева Елизавета Михайловна', 'Денисова Алиса Фёдоровна', 'Дмитриев Алексей Даниилович',
                 'Добрынин Владимир Максимович', 'Дубинина Вероника Владимировна', 'Егоров Роман Степанович', 'Егоров Григорий Егорович', 'Егорова Вероника Ивановна',
                 'Егорова Елизавета Вячеславовна', 'Емельянов Тимофей Константинович', 'Емельянова Александра Львовна', 'Ермакова Виктория Артёмовна', 'Ермолаев Даниил Семёнович',
                 'Ермолаева Ева Романовна', 'Жаров Леонид Дмитриевич', 'Завьялова Полина Марковна', 'Захаров Максим Владиславович', 'Захарова Варвара Васильевна',
                 'Захарова Ангелина Артёмовна', 'Зотова Дарья Михайловна', 'Иванов Мирон Алексеевич', 'Иванов Максим Мирославович', 'Иванов Иван Егорович',
                 'Иванова Анастасия Андреевна', 'Иванова Вероника Артёмовна', 'Иванова Алиса Алексеевна', 'Исакова Александра Тимофеевна', 'Калашников Лев Гордеевич',
                 'Калинин Виктор Ярославович', 'Карасев Артём Романович', 'Карасев Даниил Георгиевич', 'Карасев Фёдор Романович', 'Касаткин Тимофей Савельевич',
                 'Киселев Михаил Андреевич', 'Климова Дарья Степановна', 'Ковалева Мария Михайловна', 'Козина Ника Елисеевна', 'Козлова Виктория Данииловна',
                 'Козлова Анастасия Яновна', 'Комаров Дмитрий Матвеевич', 'Кондратьев Владимир Тимофеевич', 'Кондрашов Владислав Маркович', 'Константинов Вадим Иванович',
                 'Коровин Алексей Тимофеевич', 'Кравцов Матвей Даниилович', 'Круглов Алексей Владиславович', 'Крылов Илья Дмитриевич', 'Крылов Роман Максимович',
                 'Кузнецов Максим Александрович', 'Кузнецов Иван Иванович', 'Кузнецов Герман Матвеевич', 'Кузнецов Александр Даниилович', 'Кузнецова Ксения Петровна',
                 'Кузнецова Ева Алексеевна', 'Курочкин Игорь Романович', 'Лаврентьева Ксения Марковна', 'Лаврова Виктория Богдановна', 'Лазарев Роберт Георгиевич',
                 'Лебедева Алина Ярославовна', 'Лыкова Виктория Данииловна', 'Львова Елизавета Денисовна', 'Макаров Пётр Денисович', 'Максимов Евгений Никитич',
                 'Максимова Александра Владимировна', 'Матвеева Дарья Данииловна', 'Медведев Иван Михайлович', 'Мельников Роман Игоревич', 'Мельников Роман Ярославович',
                 'Мельников Андрей Михайлович', 'Мельникова Алиса Владиславовна', 'Миронов Игорь Даниилович', 'Миронова Нина Фёдоровна', 'Моисеев Никита Арсеньевич', 'Молчанова Алина Сергеевна', 'Морозова Варвара Ильинична', 'Муравьев Виктор Алексеевич', 'Назарова Елизавета Марковна', 'Нечаев Глеб Степанович', 'Нечаева Виктория Данииловна', 'Никитин Сергей Павлович', 'Никитина Александра Фёдоровна', 'Николаев Михаил Петрович', 'Николаев Дмитрий Ярославович', 'Никольский Дмитрий Даниилович', 'Новиков Максим Маркович', 'Орлов Матвей Семёнович', 'Осипова Мария Кирилловна', 'Островская Алина Фёдоровна', 'Панкратов Глеб Артёмович', 'Парамонова Ксения Яновна', 'Петров Владимир Даниилович', 'Петров Роман Викторович', 'Петров Михаил Богданович', 'Петровская Виктория Артёмовна', 'Пономарева Мария Максимовна', 'Попов Макар Борисович', 'Попов Олег Даниилович', 'Попов Даниил Артёмович', 'Попова Кира Кирилловна', 'Прохорова Анастасия Андреевна', 'Прохорова Таисия Сергеевна', 'Пугачев Глеб Фёдорович', 'Рогов Николай Львович', 'Родионов Руслан Артемьевич', 'Романов Ярослав Владимирович', 'Романов Руслан Платонович', 'Русаков Лев Савельевич', 'Русанов Кирилл Платонович', 'Рябинина Милана Михайловна', 'Рябова Анна Марковна', 'Савина Александра Васильевна', 'Севастьянова Кира Максимовна', 'Селиванова Анна Алексеевна', 'Семенова Мария Евгеньевна', 'Семенова Арина Антоновна', 'Скворцов Андрей Иванович', 'Смирнов Илья Ильич', 'Смирнов Денис Александрович', 'Смирнова Алиса Степановна', 'Смирнова Полина Святославовна', 'Смирнова Варвара Марковна', 'Соколов Дмитрий Артёмович', 'Соловьева Кира Алексеевна', 'Сорокина Мирослава Матвеевна', 'Сорокина Юлия Романовна', 'Старостин Василий Миронович', 'Судаков Лев Николаевич', 'Тихонов Денис Вячеславович', 'Трофимов Роман Иванович', 'Уткин Лев Даниилович', 'Федоров Алексей Лукич', 'Федорова Полина Матвеевна', 'Федосеева Виктория Егоровна', 'Федотов Степан Павлович',
                 'Фетисова Елизавета Михайловна', 'Филимонов Дмитрий Матвеевич', 'Фролов Иван Александрович', 'Фролова Ульяна Леонидовна',
                 'Цветков Максим Львович', 'Черкасов Степан Егорович', 'Чернова Дарья Леонидовна', 'Чернова Дарья Артёмовна',
                 'Шишкин Марк Тимофеевич', 'Шишкина Ольга Максимовна', 'Щербакова Алиса Николаевна', 'Щербакова Анна Георгиевна']

        username = generators.rnd_username(5)

        payload = {
            "Password_flag": flag,
            "email": username + "@mail.ru",
            "full_name": names[randint(0, 199)],
            "payment_method": "Default: Visa",
        }
        response = self.session.post(url, data=payload)
        return response


    def create_flag_vuln2(self, flag: str) -> str:
        
        login = "operator_ctf"
        port = "1022"
        password = "Kid238HBD1gvf19vbsu1B271vff1g"
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/bin:/bin:" + my_env["PATH"]
        #cmd = 'sshpass -p ' + password + ' ssh -p ' + port + ' ' + login + '@' + self.host + ' "echo ' + flag + ' >> /var/www/operator_temp/flags.txt"'
        #['sshpass', '-p', 'Kid238HBD1gvf19vbsu1B271vff1g', 'ssh', '-p', '22', 'root@192.168.0.104', '"echo', 'TU7ILCGQ2XP9FZQEF7LLH8Y0CW9ISK2=', '>>', '/var/www/operator_temp/flags.txt"']
        #print(cmd.split())
        result = subprocess.run(["sshpass", "-p", password, "ssh", "-o", "UserKnownHostsFile=/dev/null", "-o", "stricthostkeychecking=no", "-p", port, login + "@" + self.host, "echo " + flag + " >> /var/www/operator_temp/flags.txt"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=False, text=True, env=my_env)
        response = result.stderr
        print(result.stdout)
        print(result.stderr)
        return response

    def check_ssh_connect(self):
        login = "operator_ctf"
        port = "1022"
        password = "Kid238HBD1gvf19vbsu1B271vff1g"
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/bin:/bin:" + my_env["PATH"]
        #cmd = 'sshpass -p ' + password + ' ssh -p ' + port + ' ' + login + '@' + self.host + ' "echo ' + flag + ' >> /var/www/operator_temp/flags.txt"'
        #['sshpass', '-p', 'Kid238HBD1gvf19vbsu1B271vff1g', 'ssh', '-p', '22', 'root@192.168.0.104', '"echo', 'TU7ILCGQ2XP9FZQEF7LLH8Y0CW9ISK2=', '>>', '/var/www/operator_temp/flags.txt"']
        #print(cmd.split())
        result = subprocess.run(["sshpass", "-p", password, "ssh", "-o", "UserKnownHostsFile=/dev/null", "-o", "stricthostkeychecking=no", "-p", port, login + "@" + self.host, "id"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=False, text=True, env=my_env)
        response = result.stderr
        return response

    def get_flag_vuln1(self, flag: str) -> requests.Response:

        url = f"{self.base_url}/admin_panel/users.html"
        response = self.session.post(url)
        return response

    def get_flag_vuln2(self, flag: str) -> str:
        result1 = subprocess.run(["uname", "-a"])
        print(result1)
        login = "operator_ctf"
        port = "1022"
        password = "Kid238HBD1gvf19vbsu1B271vff1g"
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/bin:/bin:" + my_env["PATH"]
#        cmd = '/usr/bin/sshpass -p ' + password + ' ssh -p ' + port + ' ' + login + '@' + self.host + ' "cat /var/www/operator_temp/flags.txt"'
#        print(cmd)
        result = subprocess.run(["sshpass", "-p", password, "ssh", "-o", "UserKnownHostsFile=/dev/null", "-o", "stricthostkeychecking=no", "-p", port, login + '@' + self.host, "cat /var/www/operator_temp/flags.txt"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=False, text=True, env=my_env)
        print(result)
        response = result.stdout
        print(result.stderr)
        print(result.stdout)

        return response


