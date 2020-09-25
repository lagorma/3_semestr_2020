#!/bin/bash


mkdir /tmp/'hello world'/
# папка hello world в кавычках чтобы папка была с пробелом, иначе bash
# воспринимает это как два аргумента

echo hello world\!\! > /tmp/'hello world'/absolute.txt

cat /tmp/'hello world'/absolute.txt

# в свойствах absolute.sh дать разрешение на исполнение
# Все остальные аналогично:
# ~/ - домашняя директория, т.е /home/username/
# ./ - текущяя директория
# ../ - родительская директория