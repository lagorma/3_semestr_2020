#!/bin/python

import zipfile
import os
from pathlib import Path


z = zipfile.ZipFile('main.zip', 'r') #open main.zip for reading
z.extractall()   #распаковка



p=Path("main")
files=list(p.glob('**/*.py'))
out=set()
for path in files:
    out.add(path.parts[-2])

out_list=list(out)
out_list.sort()



with open('output_num3.txt','w') as plainfile:
    for line in out_list:
        plainfile.write(''.join(line)+"\n")

    
