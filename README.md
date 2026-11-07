
# Napredno programiranje

**Autor:** Ivona Dabović  
**Indeks:** 26/019  
**Studijski program:** Vještačka inteligencija

## Korišćeni alati

- Python 3.12+
- Google Colab
- pytest
- Ruff
- ChatGPT

---

## Zadatak 1 – Prosječna cijena rezervacije

### Opis

Implementirana je funkcija `prosjecna_cijena` koja učitava podatke iz CSV fajla i računa ponderisanu prosječnu cijenu noćenja.

CSV fajl sadrži kolone:
- gost
- noci
- cijena_noci

### Testiranje

Implementirana su tri testa:
- Ispravni podaci
- Prazan CSV fajl
- Neispravni podaci

Rezultat: 3 uspješna testa.

### AI prompt

„Implementiraj Python funkciju prosjecna_cijena koja učitava CSV fajl sa kolonama gost, noci i cijena_noci i računa ponderisanu prosječnu cijenu noćenja. Koristi standardnu biblioteku, type hints i obradu grešaka za prazan fajl i neispravne podatke. Prikaži kod, pytest testove i kratko objašnjenje.“

### Uočeni nedostaci i korekcije

- Provjerena je obrada neispravnih podataka.
- Dodata je provjera praznog CSV fajla.
- Ruff je prijavio neuređene i nepotrebne importe, koji su ispravljeni.
- Funkcija je testirana na tri različita slučaja.

---

## Mini projekat 1 – Refaktorisanje obrade rezervacija

### Opis

Cilj projekta je refaktorisanje monolitnog programa za obradu rezervacija primjenom principa SOLID.

Odgovornosti su razdvojene na posebne klase i funkcije:
- `Rezervacija` – predstavlja podatke o rezervaciji.
- `CsvIzvor` – učitava rezervacije iz CSV fajla.
- `TekstualniIzvjestaj` – čuva izvještaj.
- `obracunaj_iznos` – računa iznos rezervacije.
- `ObradaRezervacija` – upravlja procesom obrade.

Korišćeni su `Protocol` interfejsi za izvor podataka i izvještavanje.

### Primijenjeni principi

- **Single Responsibility Principle (SRP):** Svaka klasa ima jasno definisanu odgovornost.
- **Open/Closed Principle (OCP):** Moguće je dodati drugi izvor podataka bez izmjene servisa za obradu.
- **Dependency Inversion Principle (DIP):** Servis zavisi od protokola, a ne od konkretnih implementacija.

### Testiranje

Implementirana su tri testa:
- Obračun iznosa jedne rezervacije.
- Obrada više rezervacija.
- Obrada praznog izvora podataka.

Za testiranje su korišćeni lažni izvori podataka i lažni izvještajnik.

Rezultat: 6 uspješnih testova ukupno za oba projekta.

### AI prompt

„Ponašaj se kao iskusan softverski arhitekta. Analiziraj dati Python kod za obradu rezervacija. Identifikuj povrede SOLID principa, objasni probleme i predloži refaktorisanje razdvajanjem odgovornosti. Uvedi Protocol za izvor podataka i izvještavanje. Predloži najmanje tri pytest testa koristeći lažni izvor podataka. Izbjegavaj nepotrebne apstrakcije.“

### Uočeni nedostaci i korekcije

- Početni monolitni kod imao je više odgovornosti u jednoj klasi.
- Razdvojene su odgovornosti za učitavanje, obračun i izvještavanje.
- Uvedeni su protokoli radi lakše zamjene implementacija.
- Dodati su testovi sa lažnim izvorom i izvještajnikom.
- Ruff je korišćen za provjeru i ispravljanje kvaliteta koda.

---

## Pokretanje testova

```bash
pytest -q
