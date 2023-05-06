import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="transactions")

    cursor = connection.cursor()

    create_table1_query = '''CREATE TABLE BigTransaction
                          (ID SERIAL PRIMARY KEY,
                          NAME TEXT,
                          SUMM FLOAT,
                          CURRENCY TEXT,
                          SUMM_RUB FLOAT); '''
    
    create_table2_query = '''CREATE TABLE UsualTransaction
                          (ID SERIAL PRIMARY KEY,
                          NAME TEXT,
                          SUMM FLOAT,
                          CURRENCY TEXT,
                          SUMM_RUB FLOAT); '''
    
    cursor.execute(create_table1_query)
    cursor.execute(create_table2_query)
    connection.commit()
    print("Таблицы успешно созданы в PostgreSQL")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")