# Testprotokoll: Passwort-Validator

**Projekt:** Passwort-Validator  
**Tester/in:** ____________________  
**Datum:** ____________________  
**Bezugsdokument:** Pflichtenheft Passwort-Validator v1.0

---

## Hinweise zum Ausfüllen

- Trage in jede Zeile **einen** Testfall ein.
- **Eingabe:** Der konkrete Wert, den du testest (z. B. `"Hallo"`, `""`, `"123"`).
- **Erwartetes Ergebnis:** Was die Funktion laut Pflichtenheft zurückgeben soll.
- **Tatsächliches Ergebnis:** Was die Funktion tatsächlich zurückgibt.
- **Bestanden:** Ja/Nein — stimmen erwartet und tatsächlich überein?
- **Bemerkung:** Auffälligkeiten, Grenzfälle, Fehlerursachen.

> **Ausgangszustand:** Die Prüffunktionen `hat_mindestlaenge()`,
> `hat_grossbuchstaben()` und `hat_sonderzeichen()` sind bereits implementiert.
> Ihre Tests sind schon beim **ersten** `python -m pytest`-Lauf grün und daher
> in diesem Protokoll bereits **vorausgefüllt** (Abschnitte A1, A2 und die
> ersten drei Zeilen in A5). Die übrigen Zeilen füllst du aus, sobald du die
> zugehörige Funktion implementiert und/oder eigene Tests ergänzt hast
> (Niveau 1–3). Die Reihenfolge der Abschnitte entspricht der Ausgabe von
> `python -m pytest test_validator.py -v`.

---

## Teil A – Unit Tests (automatisiert mit pytest)

### A1 – `hat_mindestlaenge()` *(bereits implementiert – Tests ab Start grün)*

*Pflichtenheft-Referenz: F-020*

| Nr. | Eingabe                              | Erwartetes Ergebnis | Tatsächliches Ergebnis | Bestanden? | Bemerkung |
|-----|--------------------------------------|---------------------|------------------------|------------|-----------|
| 1   | `"abc"`                              | `False`             | `False`                | Ja         | Zu kurz (3 < 8) |
| 2   | `"abcdefgh"`                         | `True`              | `True`                 | Ja         | Genau Mindestlänge (8 Zeichen) |
| 3   | `"abcdefghij"`                       | `True`              | `True`                 | Ja         | Länger als Mindestlänge |
| 4   | `""`                                 | `False`             | `False`                | Ja         | Grenzfall: leerer String |
| 5   | `"abc"` mit `mindestlaenge=3`        | `True`              | `True`                 | Ja         | Benutzerdefinierte Mindestlänge |

### A2 – `hat_grossbuchstaben()` *(bereits implementiert – Tests ab Start grün)*

*Pflichtenheft-Referenz: F-030*

| Nr. | Eingabe     | Erwartetes Ergebnis | Tatsächliches Ergebnis | Bestanden? | Bemerkung |
|-----|-------------|---------------------|------------------------|------------|-----------|
| 1   | `"Hallo"`   | `True`              | `True`                 | Ja         | Ein Großbuchstabe am Anfang |
| 2   | `"hallo"`   | `False`             | `False`                | Ja         | Nur Kleinbuchstaben |
| 3   | `"HALLO"`   | `True`              | `True`                 | Ja         | Nur Großbuchstaben |
| 4   | `""`        | `False`             | `False`                | Ja         | Grenzfall: leerer String |
| 5   | `"haLlo"`   | `True`              | `True`                 | Ja         | Großbuchstabe in der Mitte |

### A3 – `hat_kleinbuchstaben()` *(selbst implementieren – Niveau 1 A1; Tests in B4 ergänzen)*

*Pflichtenheft-Referenz: F-030.
Tatsächliches Ergebnis und „Bestanden?" erst ausfüllen, nachdem die Funktion implementiert ist und `pytest` grün meldet.*

| Nr. | Eingabe      | Erwartetes Ergebnis | Tatsächliches Ergebnis | Bestanden? | Bemerkung |
|-----|--------------|---------------------|------------------------|------------|-----------|
| 1   | `"Passwort"` | `True`              |                        |            | Bereits in `test_validator.py` vorhanden |
| 2   | `"PASSWORT"` | `False`             |                        |            | Bereits in `test_validator.py` vorhanden |
| 3   |              |                     |                        |            | Eigener Testfall (B4) |
| 4   |              |                     |                        |            | Eigener Testfall (B4) |

### A4 – `hat_ziffer()` *(selbst implementieren – Niveau 1 A1; Tests in B4 ergänzen)*

*Pflichtenheft-Referenz: F-040.
Tatsächliches Ergebnis und „Bestanden?" erst ausfüllen, nachdem die Funktion implementiert ist und `pytest` grün meldet.*

| Nr. | Eingabe       | Erwartetes Ergebnis | Tatsächliches Ergebnis | Bestanden? | Bemerkung |
|-----|---------------|---------------------|------------------------|------------|-----------|
| 1   | `"Passwort1"` | `True`              |                        |            | Bereits in `test_validator.py` vorhanden |
| 2   | `"Passwort"`  | `False`             |                        |            | Bereits in `test_validator.py` vorhanden |
| 3   |               |                     |                        |            | Eigener Testfall (B4) |
| 4   |               |                     |                        |            | Eigener Testfall (B4) |
| 5   |               |                     |                        |            | Eigener Testfall (B4) |

### A5 – `hat_sonderzeichen()` *(Funktion bereits implementiert – 3 Tests ab Start grün, Tests in B4 ergänzen)*

*Pflichtenheft-Referenz: F-050*

| Nr. | Eingabe        | Erwartetes Ergebnis | Tatsächliches Ergebnis | Bestanden? | Bemerkung |
|-----|----------------|---------------------|------------------------|------------|-----------|
| 1   | `"Passw!rt"`   | `True`              | `True`                 | Ja         | Ein Sonderzeichen enthalten |
| 2   | `"Passwort1"`  | `False`             | `False`                | Ja         | Keine Sonderzeichen |
| 3   | `""`           | `False`             | `False`                | Ja         | Grenzfall: leerer String |
| 4   |                |                     |                        |            | Eigener Testfall (B4) |
| 5   |                |                     |                        |            | Eigener Testfall (B4) |

### A6 – `hash_passwort()` *(selbst implementieren – Niveau 2 B3; Test in B4 ergänzen)*

*Pflichtenheft-Referenz: F-070.
Tatsächliches Ergebnis und „Bestanden?" erst ausfüllen, nachdem die Funktion implementiert ist und `pytest` grün meldet.*

| Nr. | Eingabe / Vergleich                                  | Erwartetes Ergebnis                          | Tatsächliches Ergebnis | Bestanden? | Bemerkung |
|-----|------------------------------------------------------|----------------------------------------------|------------------------|------------|-----------|
| 1   | `"abc"`                                              | `"ba7816bf8f01cfea..."` (64 Zeichen)         |                        |            | Bekannter SHA-256-Wert, extern verifizierbar |
| 2   | `hash("Test123!") == hash("Test123!")`               | gleich (deterministisch)                     |                        |            | Gleiche Eingabe → gleicher Hash |
| 3   | `hash("passwort1") != hash("passwort2")`             | verschieden                                  |                        |            | Unterschiedliche Eingabe → anderer Hash |
| 4   | `len(hash("beliebig"))`                              | `64`                                         |                        |            | SHA-256 liefert immer 64 Hex-Zeichen |
| 5   |                                                      |                                              |                        |            | Eigener Testfall (B4) |

### A7 – Eigene Randfälle (Niveau 3, Aufgabe C2)

*Hier dokumentierst du selbst gewählte Randfälle, z. B. Umlaute, Leerzeichen, sehr lange Passwörter.
Diese Tests ergänzt du zusätzlich zu A1–A6 in `test_validator.py`.*

| Nr. | Getestete Funktion | Eingabe | Erwartetes Ergebnis | Tatsächliches Ergebnis | Bestanden? | Bemerkung |
|-----|--------------------|---------|---------------------|------------------------|------------|-----------|
| 1   |                    |         |                     |                        |            |           |
| 2   |                    |         |                     |                        |            |           |

---

## Teil B – Integrationstests (automatisiert mit pytest)

Die Klasse `TestBewertePaswort` in `test_validator.py` enthält 5 Integrationstests
für `bewerte_passwort()`. Sie werden nach der Implementierung in Niveau 2 (B2) grün.
Einen sechsten Testfall für ein **mittleres** Passwort schreibst du selbst in Aufgabe C1.

*Pflichtenheft-Referenz: F-060.
Tatsächliches Ergebnis und „Bestanden?" erst ausfüllen, nachdem `bewerte_passwort()` implementiert ist und `pytest` grün meldet.*

| Nr. | Testname                              | Eingabe       | Geprüfte Eigenschaft                                                       | Erwartetes Ergebnis                                             | Tatsächliches Ergebnis | Bestanden? | Bemerkung |
|-----|---------------------------------------|---------------|----------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|------------|-----------|
| 1   | `test_rueckgabe_ist_dict`             | `"Test123!"`  | Rückgabewert ist ein `dict`                                                | `isinstance(ergebnis, dict) == True`                            |                        |            | Formatprüfung |
| 2   | `test_alle_schluessel_vorhanden`      | `"Test123!"`  | Alle 8 Schlüssel vorhanden                                                 | `mindestlaenge`, `grossbuchstaben`, `kleinbuchstaben`, `ziffer`, `sonderzeichen`, `erfuellte_kriterien`, `punkte`, `staerke` | |            | Strukturtest |
| 3   | `test_schwaches_passwort`             | `"abc"`       | Stärke und Punkte bei schwachem Passwort                                   | `staerke == "schwach"`, `punkte <= 2`                           |                        |            | Nur Kleinbuchstaben erfüllt |
| 4   | `test_starkes_passwort`               | `"Sicher#99!"`| Stärke, erfüllte Kriterien, Punkte                                         | `staerke == "stark"`, `erfuellte_kriterien == 5`, `punkte == 6` |                        |            | Alle 5 Kriterien, Sonderzeichen doppelt gewichtet |
| 5   | `test_starkes_passwort_einzelwerte`   | `"Sicher#99!"`| Alle fünf Einzel-Booleans sind `True`                                      | je `True`                                                       |                        |            | Einzelprüfungen im Dictionary korrekt |
| 6   | *(C1: eigener Test für mittleres PW)* |               |                                                                            |                                                                 |                        |            | Eigener Testfall (C1) |

**Begründung für den selbst gewählten Testfall (Aufgabe C1):**

> *(Hier deine Begründung eintragen: Welches Passwort hast du gewählt und warum ist es „mittel"?)*

---

## Teil C – Systemtests (manuell mit `main.py`)

Starte die Anwendung mit `python main.py` und teste die folgenden Eingaben.
Der manuelle Systemtest ist erst nach Abschluss von Niveau 2 (B5) sinnvoll,
weil `main.py` vorher nicht vollständig funktioniert.

*Pflichtenheft-Referenz: F-080, F-090, F-100*

| Nr. | Eingabe      | Erwartete Stärke | Tatsächliche Stärke | Hash angezeigt? | Bestanden? | Bemerkung |
|-----|--------------|------------------|---------------------|-----------------|------------|-----------|
| 1   | `abc`        | schwach          |                     |                 |            |           |
| 2   | `Abcdefgh`   | mittel           |                     |                 |            |           |
| 3   | `Sicher#99!` | stark            |                     |                 |            |           |
| 4   | *(leer)*     | schwach          |                     |                 |            |           |
| 5   | `12345678`   | schwach          |                     |                 |            |           |
| 6   | `!@#$%^&*`   | mittel           |                     |                 |            |           |

---

## Teil D – Zusammenfassung

### Automatisierte Tests (pytest)

**Ausgangszustand (erster pytest-Lauf, vor jeder Implementierung):**

| Anzahl Tests gesamt | Bestanden | Fehlgeschlagen |
|---------------------|-----------|----------------|
| 26                  | 14        | 12             |

*Vorausgesetzt sind dabei die 14 bereits grünen Tests zu `hat_mindestlaenge()`,
`hat_grossbuchstaben()` und `hat_sonderzeichen()`; die restlichen 12 Tests
werden grün, sobald die TODO-Funktionen in Niveau 1 und 2 implementiert sind.*

**Endzustand (nach Abschluss aller Niveaus – hier eintragen):**

| Anzahl Tests gesamt | Bestanden | Fehlgeschlagen |
|---------------------|-----------|----------------|
|                     |           |                |

### Gesamtbewertung

> *Funktioniert die Anwendung insgesamt wie im Pflichtenheft beschrieben?
> Gibt es offene Fehler oder Auffälligkeiten?*

---

## Teil E – Reflexion

> **Welchen Vorteil haben automatisierte Tests (pytest) gegenüber den manuellen
> Systemtests aus Teil C? Nenne ein konkretes Beispiel aus dieser Aufgabe.**

> *(Hier deine Antwort eintragen)*
