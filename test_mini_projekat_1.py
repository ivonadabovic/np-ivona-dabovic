import pytest

from mini_projekat_1 import (
    CsvIzvor,
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
    rezervacije = [
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 2, 100),
    ]

    izvor = LazniIzvor(rezervacije)
    izvjestaj = LazniIzvjestaj()
    servis = ObradaRezervacija(izvor, izvjestaj)

    assert servis.obradi() == [240, 200]
    assert izvjestaj.iznosi == [240, 200]


def test_prazan_izvor():
    izvor = LazniIzvor([])
    izvjestaj = LazniIzvjestaj()
    servis = ObradaRezervacija(izvor, izvjestaj)

    assert servis.obradi() == []
    assert izvjestaj.iznosi == []


def test_neispravni_csv_podaci(tmp_path):
    fajl = tmp_path / "greska.csv"
    fajl.write_text(
        "gost,noci,cijena_noci\nAna,dva,100\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        CsvIzvor(fajl).ucitaj()


def test_csv_bez_potrebnih_kolona(tmp_path):
    fajl = tmp_path / "pogresan.csv"
    fajl.write_text(
        "gost,noci\nAna,3\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        CsvIzvor(fajl).ucitaj()


def test_rezervacija_sa_negativnom_cijenom():
    with pytest.raises(ValueError):
        Rezervacija("Ana", 3, -80)


def test_rezervacija_sa_nula_nocenja():
    with pytest.raises(ValueError):
        Rezervacija("Ana", 0, 80)
