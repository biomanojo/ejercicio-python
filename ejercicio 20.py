#!/usr/bin/python
# -*- coding: utf-8 -*-

ano = int(raw_input("ingresar año"))
#año= 0
if ano %4 == 0 or ano % 400 == 0:
    print "es bisiesto"
elif ano %100 !=0:
    print "no es bisiesto"

