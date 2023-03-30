from DataBase import Application, Users, Service


class FullUsersApp:

    @staticmethod
    def search_full_application_users(login: str):
        lst_out = list()
        id_users = set(item[0] for item in Users().data if item[1] == login)
        for item_app in Application().data:
            if item_app[1] == next(iter(id_users)):
                for item_ser in Service().data:
                    if item_ser[0] == item_app[2]:
                        lst_out.append([item_app[0], item_ser[1], item_ser[2], item_ser[3]])
        return lst_out
