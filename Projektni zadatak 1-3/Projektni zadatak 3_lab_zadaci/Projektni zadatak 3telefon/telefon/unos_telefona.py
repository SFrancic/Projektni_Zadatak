def unos_telefona(telefon_korisnika):
    telefon = {}
    telefon['broj'] = int(input(f"Unesite broj telefona: "))
    telefon['pozivni_broj'] = int(input(f"Unesite pozivni broj telefona: "))
    telefon['proizvodac'] = (input(f"Unesite proizvođaća telefona: "))
    return telefon
