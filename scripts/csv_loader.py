import csv

with open("../amount.csv", encoding='utf-8') as df1:
    file_reader = csv.reader(df1)
    amount  = []
    for row in file_reader:
        amount += row


with open("../clients.csv", encoding='utf-8') as df2:
    file_reader = csv.reader(df2)
    clients = []
    for row in file_reader:
        full_name = row[0].split(' ')
        surname = full_name[0]
        name = full_name[1]
        patronymic = full_name[2]

        if len(surname) > 8:
            name = ' ' + name[0] + '.'
            patronymic = patronymic[0] + '.'
            new_row = surname + name + patronymic
            clients.append(new_row)
        else:
            clients += row


with open("../currency.csv", encoding='utf-8') as df3:
    file_reader = csv.reader(df3)
    currency = []
    for row in file_reader:
        currency += row