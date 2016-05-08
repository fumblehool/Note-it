import MySQLdb
from config import db_data

def connection():
    conn = MySQLdb.connect(host=db_data['host'],
                           user=db_data['user'],
                           passwd=db_data['passwd'],
                           db=db_data['db'])
    c = conn.cursor()

    return c, conn
