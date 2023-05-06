# demo

Перенос csv данных в PostgreSQL с помощью psycopg2.

<h2>Структура проекта</h2>

- /scripts - папка со скриптами

  - csv_loader.py - загрузка данных csv

  - currency_valutes.py - получение текущих значений курса usd и eur

  - db_create.py - создание db в Postgres

  - tables.create.py - создание таблиц в db Postgres

  - combinations.py - демонстрация всевозможных комбинаций clients, amount, currency

  - data_to_db.py перенос комбинаций в db Postgres 
