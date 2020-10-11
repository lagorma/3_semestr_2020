import csv
import pandas as pd
import numpy as np
def r_csv(c):
    with open(c, 'r') as out:
        reader=csv.reader(out)
        for row in reader:
            print(row)
r_csv('table.csv')
a=pd.read_csv('table.csv', sep=';', header = 0)
a['my_col']=[True for i in range(len(a))]
a.to_csv('new_col.csv', index=False)
r_csv('new_col.csv')
