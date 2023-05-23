from datetime import date

korisnik = {}
korisnik['ime'] = input("Unesite ime korisnika: ").title()
korisnik['prezime'] = input("Unesite prezime korisnika: ").title()
korisnik['email'] = input("Unesite email korisnika: ").strip()
korisnik['telefon'] = int(input("Unesite telefon korisnika: "))

artikl = {}
artikl['naslov'] = input("Unesite naslov artikla. ")
artikl['opis'] = input("Unesite opis artikla. ")
artikl['cijena'] = int(input("Unesite cijenu artikla. "))

prodaja = {}
dan = int(input("Unesite dan prodaje: "))
mjesec = int(input("Unesite mjesec prodaje: "))
godina = int(input("Unesite godinu prodaje: "))
prodaja['datum'] = date(godina, mjesec, dan)
prodaja['artikl'] = artikl
prodaja['korisnik'] = korisnik

print("Informacije o artiklu:")
print("\tNaslov: ", prodaja['artikl']['naslov'])
print("\tOpis: ", prodaja['artikl']['opis'])
print("\tCijena: ", prodaja['artikl']['cijena'])
print("Datum isteka prodaje: ", prodaja['datum'])
print("Informacije o korisniku: ")
print("\tIme: ", prodaja['korisnik']['ime'])
print("\tPrezime: ", prodaja['korisnik']['prezime'])
print("\tEmail: ", prodaja['korisnik']['email'])
print("\tTelefon: ", prodaja['korisnik']['telefon'])