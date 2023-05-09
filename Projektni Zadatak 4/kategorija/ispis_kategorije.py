from artikl import ispis_artikla
def get_kategrija(redni_broj, kategorija):
    return f"{redni_broj}. {kategorija['naziv']}"

def ispis_svih_kategorija(kategorije):
    print("Popis kategorija: ")
    for kategorija in kategorije:
        print((f" Kategorija {kategorija['naziv']} sadrži artikle:"))
        for kategorija['artikli'] in kategorija['artikli']:
            ispis_artikla(kategorija['artikli'])
