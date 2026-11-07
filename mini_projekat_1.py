import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass
class Rezervacija:
    gost: str
    noci: int
    cijena_noci: float


class IzvorRezervacija(Protocol):
    def ucitaj(self) -> list[Rezervacija]:
        ...


class Izvjestajnik(Protocol):
    def sacuvaj(self, iznosi: list[float]) -> None:
        ...


class CsvIzvor:
    def __init__(self, putanja: Path):
        self.putanja = putanja

    def ucitaj(self) -> list[Rezervacija]:
        with open(self.putanja, encoding="utf-8") as fajl:
            reader = csv.DictReader(fajl)
            return [
                Rezervacija(
                    gost=red["gost"],
                    noci=int(red["noci"]),
                    cijena_noci=float(red["cijena_noci"]),
                )
                for red in reader
            ]


class TekstualniIzvjestaj:
    def __init__(self, putanja: Path):
        self.putanja = putanja

    def sacuvaj(self, iznosi: list[float]) -> None:
        with open(self.putanja, "w", encoding="utf-8") as fajl:
            fajl.write(f"Ukupno rezervacija: {len(iznosi)}\n")
            fajl.write(f"Ukupan iznos: {sum(iznosi):.2f} EUR\n")


def obracunaj_iznos(rezervacija: Rezervacija) -> float:
    return rezervacija.noci * rezervacija.cijena_noci


class ObradaRezervacija:
    def __init__(
        self,
        izvor: IzvorRezervacija,
        izvjestajnik: Izvjestajnik,
    ):
        self.izvor = izvor
        self.izvjestajnik = izvjestajnik

    def obradi(self) -> list[float]:
        rezervacije = self.izvor.ucitaj()
        iznosi = [
            obracunaj_iznos(rezervacija)
            for rezervacija in rezervacije
        ]
        self.izvjestajnik.sacuvaj(iznosi)
        return iznosi
