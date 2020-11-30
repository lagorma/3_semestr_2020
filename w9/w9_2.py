#!/bin/python
from zipfile import ZipFile
from pathlib import Path

class TextLoader:

    def __init__(self,way):
        with ZipFile('{}/sample.zip'.format(way),'r') as file:
            #print('{}/sample.zip'.format(way))
            file.extractall(way)
        self.way = Path('sample')
        self.files = list(el for el in list(self.way.glob('**/*')) if el.is_file())
        self.iterable = iter (self.files)


    def __len__(self):
        return len(self.files)

    def __next__(self):
        text = next(self.iterable)
        with text.open('r') as file:
            text_read = file.read()
        with text.open('w') as file:
            normal = self.norm(text_read)
            file.write(normal)
        file = text.open('r')
        return file


    def __iter__(self):
        return self


    def norm(self,s):
        s = s.lower()
        s = s.replace(',','')
        s = s.replace(';','')
        s = s.replace(':','')
        s = s.replace('.','')
        s = s.replace('?','')
        s = s.replace('!','')
        s = s.replace('-','')
        s = s.replace('(','')
        s = s.replace(')','')
        s = s.replace('"','')
        s = s.replace('/','')
        s = s.replace('—','')
        return s


way = '.'
example = TextLoader(way)
l = len(example)
print(l)
for i in range(l):
    a = next(example)
    print('text №{}'.format(i+1),a.read())

