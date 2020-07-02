import sqlite3
import uuid


class Cache:
    def __init__(self, _id):
        self._id = _id

    def __enter__(self):
        self.connector = sqlite3.connect(f"{self._id}.db")

        cursor = self.connector.cursor()
        cursor.execute("Create TABLE if not exists website(link)")
        cursor.close()

        return self

    def __exit__(self, *exc):
        self.connector.close()

    def store_link(self, link):
        cursor = self.connector.cursor()

        sql = "INSERT INTO website(link) VALUES (?)"
        cursor.execute(sql, (link,))

        self.connector.commit()
        cursor.close()

    def link_is_on_the_cache(self, link):
        sql = f"SELECT * FROM website WHERE link = '{link}'"
        cursor = self.connector.cursor()
        cursor = cursor.execute(sql)

        if cursor.fetchall() == []:
            return False

        self.connector.commit()
        cursor.close()
        return True

    def get_links(self):
        sql = "SELECT * FROM website"
        cursor = self.connector.cursor()
        cursor = cursor.execute(sql)

        links = []

        for data in cursor.fetchall():
            links.append(data[0])

        self.connector.commit()
        cursor.close()
        return tuple(links)

