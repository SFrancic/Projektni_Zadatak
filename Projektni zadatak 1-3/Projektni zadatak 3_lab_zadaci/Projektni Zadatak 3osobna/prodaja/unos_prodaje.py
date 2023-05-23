from datetime import date
from korisnik import get_korisnik
from kategorija import get_kategrija
from artikl import get_artikl
def unos_prodaje(korisnici, kategorije, redni_broj):
    prodaja = {}
    dan = int(input(f'Unesite dan isteka {redni_broj}. prodaje: '))
    mjesec = int(input(f'Unesite mjesec isteka {redni_broj}. prodaje: '))
    godina = int(input(f'Unesite godinu isteka {redni_broj}. prodaje: '))
    prodaja['datum'] = date(godina, mjesec, dan)

    print("Lista korisnika: ")
    for i, korisnik in enumerate(korisnici, start=1):
        print(get_korisnik(i, korisnik))
    odabrani_korisnik = int(input(f"Odaberite korisnika {redni_broj}. prodaje: "))
    prodaja['korisnik'] = korisnici[odabrani_korisnik-1]

    print("Lista  kategorija: ")
    for i, kategorija in enumerate(kategorije, start=1):
        print(get_kategrija(i, kategorija))
    odabrana_kategorija = int(input("Odaberite kategoriju: "))
    """prodaja['kategorija'] = kategorije[odabrana_kategorija-1]"""


    print(f"Lista artikala {redni_broj}. kategorije")
    for i, artikl in enumerate(kategorije[odabrana_kategorija-1]['artikli'], start=1):
        print(get_artikl(i, artikl))
    odabrani_artikl = int(input(f"Odaberite artikl {redni_broj}. prodaje: "))
    prodaja['artikl'] = kategorije[odabrana_kategorija-1]['artikli'][odabrani_artikl-1]
    return prodaja
