# Zadatak 1 – Prosječna cijena rezervacije

**Autor:** Ivona Dabović  
**Indeks:** 26/019  
**Predmet:** Napredno programiranje

## Opis projekta

Projekat predstavlja Python funkciju koja računa ponderisanu prosječnu cijenu noćenja na osnovu podataka iz CSV fajla.

Fajl sadrži kolone:
- gost
- noci
- cijena_noci

## Korišćeni alati

- Python 3.12+
- Google Colab
- pytest
- Ruff
- ChatGPT

## Testiranje

Pokrenuti testove komandom:

    pytest -q

Rezultat: 3 passed.

Provjera kvaliteta koda:

    ruff check main.py test_main.py

Rezultat: All checks passed.

## AI prompt

Koristila sam ChatGPT uz sljedeći zahtjev:

„Implementiraj Python funkciju prosjecna_cijena koja učitava CSV fajl sa kolonama gost, noci i cijena_noci i računa ponderisanu prosječnu cijenu noćenja. Koristi standardnu biblioteku, type hints i obradu grešaka za prazan fajl i neispravne podatke. Prikaži kod, pytest testove i kratko objašnjenje.“

## Uočeni nedostaci i korekcije

- Prva verzija nije imala potpunu obradu neispravnih podataka.
- Provjerila sam ponašanje funkcije na praznom CSV fajlu.
- Ruff je prijavio neuređene importe i jedan nepotreban import. Ispravila sam ih pomoću Ruff alata.
- Testirala sam funkciju na tri slučaja: ispravni podaci, prazan fajl i neispravni podaci.
