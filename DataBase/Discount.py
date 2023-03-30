from DataBase import DataBase


class Discount:
    def __init__(self):
        self.database = DataBase()
        self.data = self.database.conn.cursor().execute("select * from discount").fetchall()
        self.database.conn.commit()

    def new_discount(self, id_service: int, discount: int):
        self.database.conn.cursor().execute(
            f"""
            INSERT INTO discount VALUES (?, ?)
            """, id_service, discount
        )
        self.database.conn.commit()
        self.database.conn.close()

    def update_discount(self, id_discount: int, discount: int):
        self.database.conn.cursor().execute(
            f"""
            UPDATE discount set discount = {discount} where id = {id_discount}
            """
        )
        self.database.conn.commit()
        self.database.conn.close()

    def delete_discount(self, id_discount: int):
        self.database.conn.cursor().execute(
            f"""
            DELETE FROM  discount where id = {id_discount}
            """
        )
        self.database.conn.commit()
        self.database.conn.close()
