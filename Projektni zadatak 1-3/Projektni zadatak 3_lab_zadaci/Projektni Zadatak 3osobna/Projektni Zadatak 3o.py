from datetime import date
from korisnik import unos_korisnika
from kategorija import unos_kategorije
from prodaja import unos_prodaje, ispis_prodaje
from osobna import unos_osobne

korisnici = []
kategorije = []
prodaje = []
osobne = []


broj_osobnih = int(input("Unesite broj osobnih:"))
for i in range(1, broj_osobnih+1):
    osobne.append(unos_osobne(i))

broj_korisnika = int(input("Unesite broj korisnika: "))
for i in range(1, broj_korisnika+1):
    korisnici.append(unos_korisnika(i, osobne))

broj_kategorija = int(input("Unesite broj kategorija: "))
for i in range(1, broj_kategorija+1):
    kategorije.append(unos_kategorije(i))

broj_prodaja = int(input("Upisite broj prodaja: "))
for i in range(1, broj_prodaja+1):
    prodaje.append(unos_prodaje(korisnici, kategorije, i))


for i, prodaja in enumerate(prodaje, start=1):
    print(f"Informacije o {i}. prodaji: ")
    print(ispis_prodaje(prodaja, i))




