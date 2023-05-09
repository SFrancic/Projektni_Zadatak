from datetime import date

korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input("Unesite broj korisnika: "))
for i in range(1, broj_korisnika+1):
    korisnik = {}
    korisnik['ime'] = input(f'Unesite ime {i}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {i}. korisnika: ').capitalize()
    korisnik['mail'] = input(f'Unesite email {i}. korisnika: ').strip()
    korisnik['telefon'] = int(input(f'Unesite telefon {i}. korisnika: '))
    korisnici.append(korisnik)

broj_kategorija = int(input("Unesite broj kategorija: "))
for i in range(1, broj_kategorija+1):
    kategorija = {}
    artikli = []

    kategorija['naziv'] = input(f"Upisite naziv {i}. kategorije: ")
    broj_artikala = int(input(f"Upisite broj artikala za {i}. kategoriju: "))
    for j in range(1, broj_artikala+1):
        artikl = {}
        artikl['naslov'] = input(f'Unesite naslov {j}. artikla: ')
        artikl['opis'] = input(f'Unesite opis {j}. artikla: ')
        artikl['cijena'] = float(input(f'Unesite cijenu {j}. artikla: '))
        artikli.append(artikl)

    kategorija['artikli'] = artikli
    kategorije.append(kategorija)

broj_prodaja = int(input("Upisite broj prodaja: "))
for i in range(1, broj_prodaja+1):
    prodaja = {}
    dan = int(input(f'Unesite dan isteka {i}. prodaje: '))
    mjesec = int(input(f'Unesite mjesec isteka {i}. prodaje: '))
    godina = int(input(f'Unesite godinu isteka {i}. prodaje: '))
    prodaja['datum'] = date(godina, mjesec, dan)



    print(f"Odaberite korisnika {i}. prodaje: ")
    for j, korisnik in enumerate(korisnici, start = 1):
        print(f'\t{j}. {korisnik["ime"]} {korisnik["prezime"]}')

    odabrani_korisnik = int(input("Odaberite korisnika: "))



    print(f"Odaberite kategoriju {i}. prodaje: ")
    for j, kategorija in enumerate(kategorije, start=1):
        print(f'\t{j}. {kategorija["naziv"]}')

    odabrana_kategorija = int(input("Odaberite kategoriju: "))



    print(f"Odaberite artikl {i}. prodaje: ")

    for j, artikl in enumerate(kategorije[odabrana_kategorija - 1]["artikli"], start=1):
        print(f'\t{j}. {kategorije[odabrana_kategorija - 1]["artikli"][j - 1]["naslov"]}')

    odabrani_artikl = int(input("Odabrani artikl: "))

    prodaja["korisnik"] = korisnici[odabrani_korisnik - 1]
    prodaja["artikl"] = kategorije[odabrana_kategorija - 1]["artikli"][odabrani_artikl - 1]
    prodaje.append(prodaja)


for i, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}: ")
    print("Informacije o korisniku: ")
    print(f"\tIme: {prodaja['korisnik']['ime']}")
    print(f"\tPrezime: {prodaja['korisnik']['prezime']}")
    print(f"\tTelefon: {prodaja['korisnik']['telefon']}")
    print(f"\tEmail: {prodaja['korisnik']['mail']}")

    print("Informacije o artiklu: ")
    print(f"\t Naslov: {prodaja['artikl']['naslov']}")
    print(f"\t Opis: {prodaja['artikl']['opis']}")
    print(f"\t Cijena: {prodaja['artikl']['cijena']}")

    print("Datum isteka prodaje: ")
    print(f"\t Dan: {prodaja['datum'].day}")
    print(f"\t Mjesec: {prodaja['datum'].month}")
    print(f"\t Godina: {prodaja['datum'].year}")

    print('-'*20)


