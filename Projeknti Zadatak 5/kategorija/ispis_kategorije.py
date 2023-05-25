from artikl import ispis_artikla
from .kategorija import Kategorija
def get_kategrija(redni_broj, kategorija):
    return f"{redni_broj}. {kategorija.naziv}"

def ispis_svih_kategorija(kategorije):
    print("Popis svih kategorija: ")
    for kategorija in kategorije:
        kategorija.ispis()

        for j, artikl in enumerate(kategorija.artikl, start=1):
            print(f"Informacije o {j}. artiklu: ")
            artikl.ispis()
