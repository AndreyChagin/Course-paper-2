import struct

from DataBase import Application, Service
from .CalcDiscount import CalcDiscount


class SearchAppUser:
    """ Поиск заявок пользователя под своей учеткой """

    def __init__(self):
        self.__app = Application().data
        self.__service = Service().data

    def search_app(self):
        with open('settings.bin', 'rb') as file:
            __user = struct.unpack('i', file.read())[0]
        lst_out = list()
        for item_app in self.__app:
            if item_app[1] == __user:
                for item_ser in self.__service:
                    if item_ser[0] == item_app[2]:
                        lst_out.append((item_app[0], item_ser[1], CalcDiscount().calc(
                            id_service=item_ser[0],
                            price=item_ser[2]
                        ), item_ser[3]))
        return lst_out
