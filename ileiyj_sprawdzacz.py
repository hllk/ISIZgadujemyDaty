# -*- coding: utf-8 -*-

"""Dla kazdej porcji tekstu zlicza ile bylo w nim wystapien liter i, y, j. 
Nastepnie porownuje z danymi historycznymi i przewiduje rok.
Na wyjsciu wypisuje rok rzeczywisty i przewidziany."""

import re
import sys
import operator
from przewidzenie import przewidzenie

suma = 0
ile = 0

for a in sys.stdin:
    str = re.search(r'<.*annee="([0-9]*)".*', a)
    if str:
        ile = ile + 1
        rok = str.group(1)
        for a in sys.stdin:
            if re.search(r'.*<texte>.*', a):
                break
        ilei = 0
        ilej = 0
        iley = 0

        for a in sys.stdin:
            if not re.search(r'.*</texte>.*', a):
                k = re.findall(r'i', a)
                if k:
                    ilei = ilei + len(k)
            
                k = re.findall(r'j', a)
                if k:
                    ilej= ilej + len(k)
            
                k = re.findall(r'y', a)
                if k:
                    iley = iley + len(k)
            else:
                print rok
                przew =  przewidzenie(ilei, ilej, iley)                
                print przew
                print int(rok)-przew
                suma = suma + abs(int(rok)-przew)
                break

print suma/ile



