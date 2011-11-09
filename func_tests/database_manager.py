import sqlite3
from src.settings import DATABASES


class DatabaseManager(object):
    def get_connection(self):
        db = DATABASES['default']
        print db['NAME']
        return sqlite3.connect(database=db['NAME'])

    def delete_programmers(self):
        con = None
        cur = None
        try:
            con = self.get_connection()
            cur = con.cursor()
            cur.execute("DELETE FROM pair_stairs_programmer")
            con.commit()
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    def delete_pair_stairs(self):
        con = None
        cur = None
        try:
            con = self.get_connection()
            cur = con.cursor()
            cur.execute("DELETE FROM pair_stairs_pairstairs")
            con.commit()
        finally:
            if cur:
                cur.close()
            if con:
                con.close()