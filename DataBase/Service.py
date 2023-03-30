from DataBase import DataBase


class Service:
    def __init__(self):
        self.database = DataBase()
        self.data = self.database.conn.cursor().execute("select * from service").fetchall()
        self.database.conn.commit()

    def new_service(self, name: str, price: int, category: str):
        self.database.conn.cursor().execute(
            f"""
            INSERT INTO service VALUES (?, ?, ?)
            """, name, price, category
        )
        self.database.conn.commit()
        self.database.conn.close()

    def update_service(self, name: str, price:  int, id_service: int):
        if name == '' and price != 0:
            self.database.conn.cursor().execute(
                f"""
                UPDATE service SET price = {price} where id = {id_service}
                """
            )
        elif price == 0 and name != '':
            self.database.conn.cursor().execute(
                f"UPDATE service SET name_sevice = ? where id = {id_service}", name
            )
        else:
            self.database.conn.cursor().execute(
                f"""
                UPDATE service SET name_sevice = ?, price = {price} where id = {id_service}
                """, name
            )
        self.database.conn.commit()
        self.database.conn.close()
