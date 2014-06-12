# -*- coding: utf-8 -*-

"""Dla kazdej porcji tekstu zlicza słów rozpoznano, ile nie. 
Nastepnie porownuje z danymi historycznymi i przewiduje rok.
Na wyjsciu wypisuje rok rzeczywisty i przewidziany."""

import re
import sys
import operator
from przewidzenie import przewidzenie

suma = 0
ile = 0

for a in sys.stdin:
    if ile%3 == 0:
        rok = int(a)
        ile = ile + 1
    elif ile%3 == 1:
        rozp = int(a)
        ile = ile + 1
    elif ile%3==2:
        nierozp = int(a)
        ile = ile + 1
        print str(rok)
        przew = przewidzenie(rozp, nierozp)
        print str(przew)
        print int(rok)-przew
        suma = suma + abs(int(rok)-przew)

