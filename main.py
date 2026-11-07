import csv
from pathlib import Path


def prosjecna_cijena(putanja: Path) -> float:
    ukupna_cijena = 0.0
    ukupno_nocenja = 0

    with open(putanja, encoding="utf-8", newline="") as fajl:
        reader = csv.DictReader(fajl)

        for red in reader:
            try:
                cijena = float(red["cijena_noci"])
                nocenja = int(red["noci"])
            except (ValueError, TypeError, KeyError) as greska:
                raise ValueError("Neispravni podaci u CSV fajlu") from greska

            ukupna_cijena += cijena * nocenja
            ukupno_nocenja += nocenja

    if ukupno_nocenja == 0:
        raise ValueError("CSV fajl nema validnih rezervacija")

    return ukupna_cijena / ukupno_nocenja
