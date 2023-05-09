def ispis_artikla(artikl):
    print(f"\tArtikl: {artikl['naslov']} ")
    print(f"\tOpis: {artikl['opis']} ")
    print(f"\tCijena: {artikl['cijena']}")

def get_artikl(redni_broj, artikl):
    return f"{redni_broj}. {artikl['naslov']}"
