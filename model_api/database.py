from sqlalchemy import create_engine
from sqlalchemy import text
import os

engine = create_engine(os.environ["DATABASE_URL"], echo=True)
conn = engine.connect()


def check_connection():
    try:
        conn = engine.connect()
        print('Connected!')
        return True
    except:
        print('Connection failed!')
        return False


def update_request_label(req_type, req_text):
    sql = text(f'''UPDATE request
    SET type_id = (SELECT FROM types WHERE type='{req_type}')
    WHERE question = '{req_text}'
    ''')
    conn.execute(sql)
