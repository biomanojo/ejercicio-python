#! /usr/bin/env python
# -*- coding: utf-8 -*-

def caracter(letra):

    vocal = ['a', 'e', 'i', 'o', 'u']

    if letra in vocal:

        print "verde"
    else:
        print "falso"

letra = raw_input("Ingrese una opción letra: ")
print caracter(letra)