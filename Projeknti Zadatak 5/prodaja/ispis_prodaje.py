from korisnik import ispis_korisnika
from artikl import ispis_artikla
def ispis_prodaje(prodaja, redni_broj):
    print(ispis_korisnika(prodaja['korisnik']))
    print("Informacije o artiklu: ")
    print(ispis_artikla(prodaja['artikl']))

    print(f"Datum isteka {redni_broj}. prodaje : ")
    print(f"\tDan: {prodaja['datum'].day}")
    print(f"\tMjesec: {prodaja['datum'].month}")
    print(f"\tGodina: {prodaja['datum'].year}")

    print('-' * 20)

def ispis_svih_prodaja(prodaje):
    print("Popis svih prodaja: ")
    for prodaja in prodaje:
        prodaja.ispis()