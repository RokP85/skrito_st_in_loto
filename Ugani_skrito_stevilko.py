#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def skrita_stevilka():

    while True:
        secret = random.randint(0, 20)
        guess = int(raw_input("Vnesite skrito celo število, vrednosti 1-20:")) #vnos skrite stevilke
        if guess == secret:
            print "Čestitamo. Uganili ste pravo število."
        else:
            print "Napačno število"

        nadaljuj = raw_input("Želite ponovno ugibati [DA/NE]?") # možnost ponovnega ugibanja

        if nadaljuj == "NE" or nadaljuj == "ne":
            print "Hvala za igro"
            break

if __name__ == "__main__":
    skrita_stevilka()