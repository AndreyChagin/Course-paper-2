from DataBase import Service
from .CalcDiscount import CalcDiscount


class ServiceSearch:
    def __init__(self):
        self.__service = Service().data

    """ Вывод услуг по категории"""

    def service_one(self, category: str):
        lst_out = list()
        for item in self.__service:
            if item[3] == category:
                lst_out.append((item[0], item[1], item[2], item[3],
                                CalcDiscount().return_discount(item[0])))
        return lst_out

    def service_full(self):
        lst_out = list()
        for item in self.__service:
            lst_out.append((item[0], item[1], item[2], item[3],
                            CalcDiscount().return_discount(item[0])))
        return lst_out

    def return_id_service(self, name: str):
        for item in self.__service:
            if item[1] == name:
                return item[0]

    def return_name_service(self, id_service: int):
        for item in self.__service:
            if item[0] == id_service:
                return item[1]
