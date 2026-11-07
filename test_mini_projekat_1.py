
from mini_projekat_1 import (
    ObradaRezervacija,
    Rezervacija,
    obracunaj_iznos,
)


class LazniIzvor:
    def __init__(self, rezervacije):
        self.rezervacije = rezervacije

    def ucitaj(self):
        return self.rezervacije


class LazniIzvjestaj:
    def __init__(self):
        self.iznosi = None

    def sacuvaj(self, iznosi):
        self.iznosi = iznosi


def test_obracun_iznosa():
    rezervacija = Rezervacija("Ana", 3, 80)
    assert obracunaj_iznos(rezervacija) == 240


def test_obrada_vise_rezervacija():
    izvor = LazniIzvor([
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 2, 100),
    ])
    izvjestaj = LazniIzvjestaj()

    servis = ObradaRezervacija(izvor, izvjestaj)
    rezultat = servis.obradi()

    assert rezultat == [240, 200]
    assert izvjestaj.iznosi == [240, 200]


def test_prazan_izvor():
    izvor = LazniIzvor([])
    izvjestaj = LazniIzvjestaj()

    servis = ObradaRezervacija(izvor, izvjestaj)
    rezultat = servis.obradi()

    assert rezultat == []
    assert izvjestaj.iznosi == []
