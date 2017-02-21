#! /usr/bin/env python
# -*- coding: utf-8 -*-

def inversa():
    cadena = raw_input("Ingrese una palabra: ")
    var = ''
    for h in cadena:
        var = h + var

    print var


inversa()