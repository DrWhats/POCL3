from sqlalchemy import create_engine
from sqlalchemy import text
import os
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine(os.environ["DATABASE_URL"], echo=True)
conn = engine.connect()


try:
    conn = engine.connect()
    print('Connected!')
except:
    print('Connection failed!')


def check_user(email, password):
    sql = text(f"SELECT email, password FROM user WHERE email = '{email}'")
    res = conn.execute(sql).fetchone()
    print(res[0] + " " + res[1])
    if check_password_hash(res[1], password):
        return True


def save_user(email, tg_login):
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
    conn.commit()
    conn.close()
    print('Успешно зарегистрирован')


def show_users():
    conn = engine.connect()
    sql = text("SELECT * FROM moderator")
    res = conn.execute(sql).fetchall()
    return res
