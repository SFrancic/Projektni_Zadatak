from datetime import date

korisnici = []
kategorije = []
prodaje = []
artikli = []

def unos_korisnika(redni_broj):
    korisnik = {}
    korisnik['ime'] = input(f'Unesite ime {i}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {i}. korisnika: ').capitalize()
    korisnik['email'] = input(f'Unesite email {i}. korisnika: ').strip()
    korisnik['telefon'] = int(input(f'Unesite telefon {i}. korisnika: '))
    return korisnik

def ispis_korisnika(korisnik):
    print(f"\tKorisnik: {korisnik['ime']} {korisnik['prezime']}")
    print(f"\t email: {korisnik['email']}")
    print(f"\t telefon: {korisnik['telefon']}")


def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik['ime']} {korisnik['prezime']}"

def unos_artikla(redni_broj):
    artikl = {}
    artikl['naslov'] = input(f'Unesite naslov {redni_broj}. artikla: ')
    artikl['opis'] = input(f'Unesite opis {redni_broj}. artikla: ')
    artikl['cijena'] = int(input(f'Unesite cijenu {redni_broj}. artikla: '))
    return artikl

def ispis_artikla(artikl):
    print(f"\tArtikl: {artikl['naslov']} ")
    print(f"\tOpis: {artikl['opis']} ")
    print(f"\tCijena: {artikl['cijena']}")

def get_artikl(redni_broj, artikl):
    return f"{redni_broj}. {artikl['naslov']}"

def unos_kategorije(redni_broj):
    kategorija = {}
    kategorija['naziv'] = input(f"Upisite naziv {redni_broj}. kategorije: ")
    kategorija['artikli'] = []

    broj_artikala = int(input(f"Upisite broj artikala za {redni_broj}. kategoriju: "))
    for i in range(1, broj_artikala + 1):
        artikl = unos_artikla(i)
        kategorija['artikli'].append(artikl)
    return kategorija

def get_kategrija(redni_broj, kategorija):
    return f"{redni_broj}. {kategorija['naziv']}"

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

def ispis_prodaje(prodaja):
    print(ispis_korisnika(prodaja['korisnik']))

    print("Informacije o artiklu: ")
    print(ispis_artikla(prodaja['artikl']))

    print(f"Datum isteka {i}. prodaje : ")
    print(f"{prodaja['datum']}")

    print('-' * 20)

broj_korisnika = int(input("Unesite broj korisnika: "))
for i in range(1, broj_korisnika+1):
    korisnici.append(unos_korisnika(i))

broj_kategorija = int(input("Unesite broj kategorija: "))
for i in range(1, broj_kategorija+1):
    kategorije.append(unos_kategorije(i))

broj_prodaja = int(input("Upisite broj prodaja: "))
for i in range(1, broj_prodaja+1):
    prodaje.append(unos_prodaje(korisnici, kategorije, i))


for i, prodaja in enumerate(prodaje, start=1):
    print(f"Informacije o {i}. prodaji: ")
    print(ispis_prodaje(prodaja))




