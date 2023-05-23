from utilities import unos_pozitivnog_cijelog_broja
from vozacka import unos_vozacke
def unos_korisnika(redni_broj):
    korisnik = {}
    korisnik['ime'] = input(f"Unesite ime {redni_broj}. korisnika: ").capitalize()
    korisnik['prezime'] = input(f"Unesite prezime {redni_broj}. korisnika: ").capitalize()
    korisnik['email'] = input(f"Unesite email {redni_broj}. korisnika: ").strip()
    korisnik['telefon'] = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika: ")
    korisnik['vozacka'] = unos_vozacke(redni_broj)
    return korisnik