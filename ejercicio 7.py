#! /usr/bin/env python
# -*- coding: utf-8 -*-

def palindromo():
    cadena = raw_input("Ingrese una palabra: ")
    var = ''
    for h in cadena:
        var = h + var
    if var == cadena :
        print "es polindroma"
    else:
        print "falso"

palindromo()