"""
Oefening 5: Raad Het Getal

Doel: while-loops, condities en input() combineren.

Let op de int() rondom input(): input() geeft altijd tekst (string) terug,
dus we moeten het omzetten naar een getal (integer) om te kunnen vergelijken
met 'geheim'.
"""

geheim = 7
gok = int(input("Raad het getal: "))

while gok != geheim:
    print("Dat was niet het getal, nog een poging!")
    gok = int(input("Raad het getal: "))

print("Je hebt het geraden! 🎉")
