from pyodbc import connect


class DataBase:
    def __init__(self):
        self.conn = connect("Driver={SQL Server}; Server=*; Trusted_Connection=True; Database=course")