# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.

import csv
from random import randint
file = 'pull.csv'

with open(file, 'w+', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['COLUMN1','COLUMN2','COLUMN3'])
    writer.writeheader()
    for i in range(1,100):
        tmp_dict = {f'COLUMN{i}': randint(1,100) for i in range(1,4)}
        writer.writerow(tmp_dict)
