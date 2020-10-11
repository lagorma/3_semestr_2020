import csv
def r_csv(c):
    with open(c, 'r') as out:
        reader = csv.reader(out)
        for row in reader:
            print(row)
r_csv('table.csv')


import pandas as pd
import numpy as np
a= pd.read_csv('table.csv', sep = ';', header = None)
b=pd.DataFrame(np.insert(a.values, int(len (a)/2), values = [-200, -200, -200, -200], axis =0))
b.to_csv('middle_row.csv', index = False, header=0)
r_csv('middle_row.csv')



