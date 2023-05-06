from combinations import get_combinations
import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="transactions")

    cursor = connection.cursor()
    for row in get_combinations():
        if row[3] > 1000:
            insert_query = "INSERT INTO BigTransaction (NAME, SUMM, CURRENCY, SUMM_RUB) VALUES (%s, %s, %s, %s)"              
            cursor.execute(insert_query, (row[0], row[1], row[2], row[3]))
            connection.commit()
        else:
            insert_query = "INSERT INTO UsualTransaction (NAME, SUMM, CURRENCY, SUMM_RUB) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (row[0], row[1], row[2], row[3]))
            connection.commit()
    print("Таблицы успешно обновлены")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")