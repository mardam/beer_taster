from datetime import datetime
import os
import sqlite3

class DatabaseConnector:
    def __init__(self, path):
        self.path = path
        if (not os.path.exists(path)):
            self.create_database()

    def create_database(self):
        print("create database")
        conn = self.connect()
        conn.execute("CREATE TABLE beer (id integer PRIMARY KEY, name varchar(20), brand varchar(20), type varchar(20))")
        conn.execute("CREATE TABLE judgement (id integer PRIMARY KEY, beer integer, user TEXT, colour integer, foam integer, taste integer, posttaste integer, bottle integer, time DATE)")
        conn.close()

    def connect(self):
        return sqlite3.connect(self.path)

    def execute_insert_query(self, query):
        conn = self.connect()
        conn.execute(query)
        conn.commit()
        conn.close()

    def insert_beer(self, id: int, name: str, brand: str, type: str):
        query = f"INSERT INTO beer (id, name, brand, type) VALUES ({id}, '{name}', '{brand}', '{type}')"
        self.execute_insert_query(query)

    def insert_judgement(self, beer: int, user: str, colour: int, foam: int, taste: int, posttaste: int, bottle: int):
        time = datetime.now().isoformat()
        query = f"INSERT INTO judgement (beer, user, colour, foam, taste, posttaste, bottle, time) VALUES ({beer}, '{user}', {colour}, {foam}, {taste}, {posttaste}, {bottle}, '{time}')"
        print(query)
        self.execute_insert_query(query)

if __name__ == "__main__": 
    dc = DatabaseConnector("database.db")
    dc.insert_beer(1, "abc", "def", "fgh")
    dc.insert_judgement(1, "Markus", 1, 2, 3, 4, 5)

