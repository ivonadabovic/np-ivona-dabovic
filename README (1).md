# Mini projekat 1 – SOLID refaktorisanje obrade rezervacija

## Opis projekta

Cilj projekta je refaktorisanje sistema za obradu rezervacija primjenom SOLID principa. Sistem učitava podatke o rezervacijama iz CSV fajla, obračunava ukupne iznose i čuva izvještaj.

## Funkcionalnosti

- Učitavanje rezervacija iz CSV fajla.
- Provjera ispravnosti podataka.
- Validacija imena gosta, broja noćenja i cijene.
- Obračun ukupnog iznosa rezervacije.
- Generisanje tekstualnog izvještaja.
- Obrada praznog izvora podataka.

## Struktura projekta

- `mini_projekat_1.py` – glavna implementacija.
- `test_mini_projekat_1.py` – automatski testovi.
- `README.md` – dokumentacija projekta.

## Primjena SOLID principa

**Single Responsibility Principle (SRP)**

Svaka klasa ima jasno definisanu odgovornost:
- `CsvIzvor` učitava podatke iz CSV fajla.
- `TekstualniIzvjestaj` čuva izvještaj.
- `ObradaRezervacija` upravlja procesom obrade.
- `Rezervacija` predstavlja podatke o jednoj rezervaciji.

**Dependency Inversion Principle (DIP)**

Klasa `ObradaRezervacija` zavisi od apstrakcija definisanih pomoću `Protocol`, a ne od konkretnih implementacija.

Protokoli:
- `IzvorRezervacija`
- `Izvjestajnik`

Na ovaj način moguće je koristiti različite izvore podataka i načine čuvanja izvještaja bez izmjene glavne klase za obradu.

## Pokretanje testova

Za instalaciju potrebnih alata:

```bash
pip install pytest ruff
```

Pokretanje testova:

```bash
pytest -q
```

Provjera kvaliteta koda:

```bash
ruff check mini_projekat_1.py test_mini_projekat_1.py
```

## Testiranje

Projekat sadrži 7 automatskih testova koji provjeravaju:
- obračun iznosa rezervacije;
- obradu više rezervacija;
- obradu praznog izvora;
- neispravne podatke u CSV fajlu;
- nedostajuće CSV kolone;
- negativnu cijenu;
- nula noćenja.

Rezultat testiranja: **7 passed**.

## Korišćenje AI alata

AI alat je korišćen kao pomoć pri razumijevanju SOLID principa, refaktorisanju koda, organizaciji testova i otklanjanju grešaka.

Predložena rješenja su provjerena kroz izvršavanje programa, automatske testove i Ruff alat.

## Zaključak

Refaktorisanjem je postignuta bolja organizacija koda, jasnije razdvajanje odgovornosti i lakše testiranje. Zahvaljujući protokolima, sistem je fleksibilniji i jednostavniji za proširivanje.
