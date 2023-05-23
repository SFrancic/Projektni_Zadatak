from vozacka import ispis_vozacke
def ispis_korisnika(korisnik):
    print(f"\tKorisnik: {korisnik['ime']} {korisnik['prezime']}")
    print(f"\t email: {korisnik['email']}")
    print(f"\t telefon: {korisnik['telefon']}")
    '''ispis_telefona(korisnik['telefon'])'''
    ispis_vozacke(korisnik['vozacka'])

def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik['ime']} {korisnik['prezime']}"

def ispis_svih_korisnika(korisnici):
    print("Popis korisnika: ")
    for korisnik in korisnici:
        ispis_korisnika(korisnik)
