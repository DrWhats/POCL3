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


def get_type_moders(type):
    sql = text(f'SELECT tg FROM moderator WHERE typeId = {type}')
    results = conn.execute(sql).fetchall()
    tg_list = [result['tg'] for result in results]
    return tg_list


def get_type_by_label(label):
    sql = text(f'SELECT id FROM types WHERE type = {label}')
    res = conn.execute(sql).fetchone()
    if res:
        type_id = res['id']
        return type_id
    else:
        return None
