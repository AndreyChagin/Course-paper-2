from DataBase import Discount


class CalcDiscount:
    @staticmethod
    def calc(id_service: int, price: int):
        for item in Discount().data:
            if item[1] == id_service:
                return int(price - price * (item[2] / 100))
        else:
            return int(price)

    @staticmethod
    def return_discount(id_service: int):
        for item in Discount().data:
            if item[1] == id_service:
                return f"{item[2]}%"
        else:
            return '-'
