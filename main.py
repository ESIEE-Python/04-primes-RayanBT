"""
Ce module contient une fonction pour vérifier si un nombre est premier.
"""

from math import sqrt

def isprime(p):
    """
    Vérifie si un nombre est un nombre premier.

    Args:
        p (int): Le nombre à tester.

    Returns:
        bool: True si p est premier, False sinon.
    """

    if p <= 1:
        return False
    if p <= 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False

    max_check = int(sqrt(p))  # Vérifie jusqu'à la racine carrée de p
    i = 5
    while i <= max_check:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True


#### Fonction principale


def main():
    """
    Point d'entrée principal du programme.    
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
