#!/usr/bin/python
# -*- coding: utf-8 -*-


def c_mayusculas ():
    palabra1 = raw_input("Nombres palabra")
    cont = 0
    for i in palabra1:
        if i != i.lower(): #Recordar que lower() convierte una cadena en minúsculas
            cont += 1
    print "La cadena tiene", cont, "mayuscula/s"

c_mayusculas()