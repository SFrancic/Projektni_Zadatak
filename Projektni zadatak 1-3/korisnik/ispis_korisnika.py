def ispis_korisnika(korisnik):
    print(f"\tKorisnik: {korisnik['ime']} {korisnik['prezime']}")
    print(f"\t email: {korisnik['email']}")
    print(f"\t telefon: {korisnik['telefon']}")


def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik['ime']} {korisnik['prezime']}"
