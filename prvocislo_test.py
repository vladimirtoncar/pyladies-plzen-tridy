# Jednoduchy test, zda je zadane cislo prvocislem.

def je_prvocislo(cislo):
    # Kdyz je mensi nebo rovno 1, neni to prvocislo
    if cislo <= 1:
        return False
    # Ted zkousime, jestli je delitelne cimkoli 
    # mezi 2 az po (cislo-1)
    for i in range(2, cislo):
        if (cislo % i) == 0:
            # Je delitelne aktualni hodnotou i
            # takze to neni prvocislo
            return False
    # end for

    # Kdyz jsme dosli sem, nenasli jsme zadnou delitelnost
    return True
# end def


