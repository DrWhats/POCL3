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


# TODO: вытягивать по айдишнику, а не по тексту запроса, так как они могут быть одинаковыми
def update_request_label(req_type, req_text):
    sql = text(f'''UPDATE request
    SET typeId = (SELECT id FROM types WHERE type='{req_type}')
    WHERE question = '{req_text}'
    ''')
    conn.execute(sql)


# TODO: вытягивать по айдишнику, а не по тексту запроса, так как они могут быть одинаковыми
def get_full_request(req_text):
    sql = text(f'''SELECT * FROM request
        WHERE question = '{req_text}'
        ''')
    result = conn.execute(sql).fetchone()
    return result


def get_type_moders(type):
    sql = text(f"SELECT tg FROM moderator WHERE typeId = {type}")
    results = conn.execute(sql).fetchall()
    tg_list = [result[0] for result in results]
    return tg_list


def get_type_by_label(label):
    sql = text(f"SELECT id FROM types WHERE type = '{label}'")
    res = conn.execute(sql).fetchone()
    if res:
        type_id = res[0]
        return type_id
    else:
        return None
