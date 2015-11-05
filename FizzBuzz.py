# -*- coding: utf-8 -*-

while True:
    vpisano_stevilo = int(raw_input("Vpisi poljubno stevilo med 1 in 100: "))
    if vpisano_stevilo > 0 and vpisano_stevilo <= 100:
        for x in range(1, vpisano_stevilo + 1):
            if x % 3 == 0 and x % 5 != 0:
                print "fizz"
            elif x % 5 == 0 and x % 3 != 0:
                print "buzz"
            elif x % 3 == 0 and x % 5 == 0:
                print "fizzbuzz"
            elif x % 3 != 0 and x % 5 != 0:
                print x
        break
    else:
        print "Vnesti moras stevilo med 1 in 100!"