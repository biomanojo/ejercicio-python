#!/usr/bin/python
# -*- coding: utf-8 -*-
num = int(raw_input("ingresa un número entre 1 a 100000 :\n>>"))
cont=0
numero = str(num)

for i in numero:
    cont+=1
    print "el numero consta de ", cont, " digitos "
    #um = int(numero)