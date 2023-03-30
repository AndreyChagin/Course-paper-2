from pyodbc import connect


class DataBase:
    def __init__(self):
        self.conn = connect("Driver={SQL Server}; Server=D*SKTOP-E1HH3A6; Trusted_Connection=True; Database=course")