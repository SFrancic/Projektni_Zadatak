from korisnik import ispis_korisnika
from artikl import ispis_artikla
def ispis_prodaje(prodaja, redni_broj):
    print(ispis_korisnika(prodaja['korisnik']))

    print("Informacije o artiklu: ")
    print(ispis_artikla(prodaja['artikl']))

    print(f"Datum isteka {redni_broj}. prodaje : ")
    print(f"{prodaja['datum']}")

    print('-' * 20)