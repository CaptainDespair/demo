import itertools

from csv_loader import clients, amount, currency
from currency_valutes import get_current_eur_rate, get_current_usd_rate

NUM_ROUNDED_DIG = 2

def get_combinations():
    combinations = [list(comb) for comb in\
                    itertools.product(clients, amount, currency)]
    for row in combinations:
        if row[2] == 'RUB':
            row.append(float(row[1]))
            row.append('RUB')
        elif row[2] == 'USD':
            row.append(round(int(row[1])*get_current_usd_rate(), 
                             NUM_ROUNDED_DIG))
            row.append('RUB')
        elif row[2] == 'EUR':
            row.append(round(int(row[1])*get_current_eur_rate(), 
                             NUM_ROUNDED_DIG))
            row.append('RUB')
    return combinations

if __name__ == '__main__':
    print('Всевозможные комбинации:\n')
    for row in get_combinations():
        print(row)
