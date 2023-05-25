class Korisnik:
    def __init__(self, ime, prezime, email, telefon):
        self.__ime = ime
        self.__prezime = prezime
        self.__email = email
        self.__telefon = telefon

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def email(self):
        return self.__email

    @property
    def telefon(self):
        return self.__telefon

    def ispis(self):
        print(f"\tKorisnik: {self.ime} {self.prezime}")
        print(f"\t email: {self.email}")
        print(f"\t telefon: {self.telefon}")
