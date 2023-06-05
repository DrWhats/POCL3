from sqlalchemy import create_engine
from sqlalchemy import text
import os

engine = create_engine(os.environ["DATABASE_URL"], echo=True)


def check_connection():
    try:
        conn = engine.connect()
        print('Connected!')
        return True
    except:
        print('Connection failed!')
        return False


def get_all_types():
    conn = engine.connect()
    sql = text("SELECT type FROM types")
    res = conn.execute(sql).fetchall()
    resarr = ""
    for record in res:
        resarr += record[0] + ","
    return resarr