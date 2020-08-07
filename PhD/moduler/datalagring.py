import sqlite3
import pandas as pd

class minDatabase:


    @staticmethod
    def oppretteDB():
        c = conn.cursor()
        c.execute("""CREATE TABLE prove (
                        first text,
                        last text
                        )""")
        conn.commit()

    @staticmethod
    def lagreiDB(df):
        conn = sqlite3.connect('data.db')
        conn.commit()
        df.to_sql('treningsokter', conn, if_exists='append')


