# -*- coding: utf-8 -*-

"""przygotowuje teksty z dev do sprawdzenia"""

import re
import sys


wejscie = open('retroc-dev-cleaned-500w.xml', 'r')


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
            nazwa = 'dev/' + repr(licznik) + '.txt'
            plik = open(nazwa, 'a')
            plik.write(rok + '\n')
            plik.write(tresc)
    line = wejscie.readline()

        

