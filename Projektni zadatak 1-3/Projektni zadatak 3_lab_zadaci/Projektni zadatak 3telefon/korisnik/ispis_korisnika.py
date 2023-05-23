from telefon import ispis_telefona
def ispis_korisnika(korisnik):
    print(f"\tKorisnik: {korisnik['ime']} {korisnik['prezime']}")
    print(f"\t email: {korisnik['email']}")
    ispis_telefona(korisnik['telefon'])

def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik['ime']} {korisnik['prezime']}"
