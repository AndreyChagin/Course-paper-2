from DataBase import DataBase


class Users:
    def __init__(self):
        self.database = DataBase()
        self.data = self.database.conn.cursor().execute("select * from users").fetchall()
        self.database.conn.commit()

    def new_user(self, login: str, password: str, phone: str):
        self.database.conn.cursor().execute(f"INSERT INTO users (login, password, phone) VALUES (?, ?, ?)",
                                            login, password, phone)
        self.database.conn.commit()
        self.database.conn.close()
