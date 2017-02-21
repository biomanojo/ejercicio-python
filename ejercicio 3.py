#!/usr/bin/python
# -*- coding: utf-8 -*-


def palabra():
    palabra1 = raw_input("Nombres palabra")

    cont = 0

    for i in palabra1:
        cont += 1
        print(" " + str(cont))

palabra()
