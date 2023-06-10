from sqlalchemy import create_engine
from sqlalchemy import text
import os
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine(os.environ["DATABASE_URL"], echo=True)


def check_connection():
    try:
        conn = engine.connect()
        print('Connected!')
        return True
    except:
        print('Connection failed!')
        return False


def check_user(email, password):
    conn = engine.connect()
    sql = text(f"SELECT email, password FROM User WHERE email = '{email}'")
    res = conn.execute(sql).fetchone()
    print(res[0] + " " + res[1])
    if check_password_hash(res[1], password):
        return True

def save_user(email, tg_login):
    conn = engine.connect()
    sql = text(f'''
               UPDATE moderator 
               SET tg = '{tg_login}' 
               WHERE userId = (
                SELECT id
                FROM user
                WHERE email = '{email}'
               )
            ''')
    conn.execute(sql)
    print('Успешно зарегистрирован')
