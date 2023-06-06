def ispis_korisnika(korisnik):
    print(f"\tKorisnik: {korisnik['ime']} {korisnik['prezime']}")
    print(f"\t email: {korisnik['email']}")
    print(f"\t telefon: {korisnik['telefon']}")

def get_korisnik(redni_broj, korisnik):
    return f"Email: {redni_broj}. korisnika: {korisnik.email} \nTelefon {redni_broj}. korisnika: {korisnik.telefon}"

def ispis_svih_korisnika(korisnici):
    print("Popis svih korisnika: ")
    for korisnik in korisnici:
        korisnik.ispis()
