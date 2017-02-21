#!/usr/bin/python
# -*- coding: utf-8 -*-

def palabra():
    palabra1 = raw_input("Nombres palabra")

    cont = 0
    cont2 = 0
    for i in palabra1:
        cont += 1
        print(" " + str(cont))
    palabra2 = raw_input("¿ingrese palabra ")
    for i in palabra2:
        cont2 += 1
        print(" " + str(cont2))
    if cont >= cont2 :
        print "el mayor numero de palabra en ",str(palabra1)
    elif cont <= cont2:
         print "el mayor numero de palabra en ",str(palabra2)

palabra()