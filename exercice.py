#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    mon_nombre = float(input('Veuillez saisir un nombre: '))
    if mon_nombre < 0:
        valeur_absolue = -mon_nombre
    else:
        valeur_absolue = mon_nombre

    return valeur_absolue


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    resultat = []
    for prefixes in prefixes:
        nom = prefixes + suffixes
        resultat.append(nom)
    return resultat


def prime_integer_summation() -> int:
    nombre_premier= 0
    nombre = 2
    sommes = 0
    while nombre_premier < 100:
        est_premier = True
        for i in range(1, nombre + 1):
            if (nombre % i == 0 and i != 1 and i != nombre):
                est_premier = False
                break
        if  est_premier:
                nombre_premier += 1
                sommes += nombre
        nombre += 1
    return sommes

def factorial(number: int) -> int:
    factorielle = 1
    for i in range(1, number+1):
        factorielle = factorielle*i
    print(factorielle)
    return factorielle


def use_continue() -> None:
    for i in range(1,11):
        if i==5:
           continue
        print(i)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
