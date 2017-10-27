#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Pozdravljeni v generatorju loto števil"

import random

generirane_stevilke = []
vnos = int(raw_input("Koliko števil želite pri žrebu ?:"))

while True:     # zanka za generiranje nabora števil
    if len(generirane_stevilke) == vnos:
            break

    stevilka = random.randint(0, 50)

    if stevilka not in generirane_stevilke:
        generirane_stevilke.append(stevilka)

print "Izžrebane so številke: %s" % (generirane_stevilke)