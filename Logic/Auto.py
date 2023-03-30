import struct

from DataBase import Users


class Autorization:
    """ Авторизация """
    def __init__(self):
        self.lst_users = Users().data

    def proverka(self, login: str, password: str):
        for x in self.lst_users:
            if x[1] == login and password == x[2] and x[3] is not None:
                with open("settings.bin", "wb") as file:
                    file.write(struct.pack('i', x[0]))
                return 'Users'
            elif x[1] == login and password == x[2] and x[3] is None:
                return 'Manager'

