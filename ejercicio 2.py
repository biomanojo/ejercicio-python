#!/usr/bin/python
# -*- coding: utf-8 -*-

def mayor():
    a = int(input('ingrese un numero '))
    b = int(input('ingrese un numero '))
    c = int(input('ingrese un numero '))
    if a > b and a>c:
         print('el mayor es ',a)
    elif a < b and b > c:
         print('el mayor es ',b)
    elif a < c and b < c:
         print('el mayor es ',c)
mayor()