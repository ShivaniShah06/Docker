from database import database_url
import psycopg2

def check_db_connection():
    try:
        db_connection = psycopg2.connect(database_url)
        db_connection.close()
        return True
    except Exception as e:
        return False