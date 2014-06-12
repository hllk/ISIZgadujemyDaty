# -*- coding: utf-8 -*-


import re
import sys


wejscie = open('retroc-train-cleaned-500w.xml', 'r')

"""
for i in range (1775, 2014):
    plik = open.Lata[i] = 0

Lata[1497] = 0
Lata[1391] = 0
Lata[1670] = 0
Lata[1650] = 0
Lata[1686] = 0
"""

line = wejscie.readline()
licznik = 0

while line:
    str = re.search(r'<.*annee="([0-9]*)".*', line)
    if str:
        rok = str.group(1)
        tresc = ""
        line = wejscie.readline()
        line = wejscie.readline()
        line = wejscie.readline()
        while not(re.search(r'.*</texte>.*', line)):
            tresc = tresc + line
            line = wejscie.readline()
        else:
            print licznik
            licznik = licznik + 1
            plik = open('tresci/'+rok+'.txt', 'a')
            plik.write(tresc)
    line = wejscie.readline()

        

