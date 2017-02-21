#! /usr/bin/env python
# -*- coding: utf-8 -*-

def superposicion():
    cadena1 = raw_input("Ingrese una palabra: ")
    cadena2 = raw_input("Ingrese una palabra: ")

    for i in cadena1:
        for j in cadena2:
            if i == j:
                print "verdadero"


    print "falso"
superposicion()