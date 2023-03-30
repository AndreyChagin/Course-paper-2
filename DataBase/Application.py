import struct

from DataBase import DataBase


class Application:
    def __init__(self):
        self.database = DataBase()
        self.data = self.database.conn.cursor().execute("select * from app").fetchall()
        self.database.conn.commit()

    def new_app(self, id_service):
        with open('settings.bin', 'rb') as file:
            users = struct.unpack('i', file.read())[0]
        self.database.conn.cursor().execute("INSERT INTO app (id_users, id_service) values (?, ?)",
                                            users, id_service)
        self.database.conn.commit()
        self.database.conn.close()

    def delete_application(self, id_app: int):
        self.database.conn.cursor().execute(
            f"""
            DELETE from app where id = ? 
            """, id_app
        )
        self.database.conn.commit()
        self.database.conn.close()


