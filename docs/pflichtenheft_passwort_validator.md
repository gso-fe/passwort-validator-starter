# Pflichtenheft: Passwort-Validator

**Projekt:** Passwort-Validator  
**Version:** 1.0  
**Datum:** April 2026  
**Auftraggeber:** Fachabteilung IT-Sicherheit (fiktiv)  
**Auftragnehmer:** Entwicklungsteam (Lernende)

---

## 1 Zielbestimmung

Es soll ein Python-Modul entwickelt werden, das Passwörter automatisiert auf
Sicherheitskriterien prüft, bewertet und sicher hasht. Das Modul wird als
Bibliothek (`validator.py`) bereitgestellt und von einer Konsolenanwendung
(`main.py`) genutzt.

---

## 2 Produkteinsatz

| Merkmal        | Beschreibung                                    |
|----------------|-------------------------------------------------|
| Anwendungsbereich | Prüfung und Bewertung von Benutzerpasswörtern |
| Zielgruppe     | Endanwender über eine Konsolenanwendung         |
| Betriebsumgebung | Python 3.10+, Windows/Linux/macOS              |

---

## 3 Funktionale Anforderungen

### 3.1 Einzelprüfungen

Das Modul muss folgende Prüffunktionen bereitstellen.
Jede Funktion erhält ein Passwort (String) und gibt `True` oder `False` zurück.

| ID    | Funktion              | Beschreibung                                           |
|-------|-----------------------|--------------------------------------------------------|
| F-010 | `hat_mindestlaenge`   | Prüft, ob das Passwort mindestens 8 Zeichen lang ist. Die Mindestlänge soll über einen optionalen Parameter konfigurierbar sein (Standard: 8). |
| F-020 | `hat_grossbuchstaben` | Prüft, ob mindestens ein Großbuchstabe (A–Z) enthalten ist. |
| F-030 | `hat_kleinbuchstaben` | Prüft, ob mindestens ein Kleinbuchstabe (a–z) enthalten ist. |
| F-040 | `hat_ziffer`          | Prüft, ob mindestens eine Ziffer (0–9) enthalten ist.  |
| F-050 | `hat_sonderzeichen`   | Prüft, ob mindestens ein Sonderzeichen aus dem definierten Zeichensatz enthalten ist. Der Zeichensatz lautet: `!@#$%^&*()_+-=[]{}|;':\",./<>?` |

### 3.2 Passwortbewertung

| ID    | Funktion            | Beschreibung                                             |
|-------|---------------------|----------------------------------------------------------|
| F-060 | `bewerte_passwort`  | Bewertet ein Passwort anhand aller fünf Einzelprüfungen und gibt ein Dictionary mit Einzelergebnissen, Punktzahl und Stärkeklasse zurück. |

**Gewichtung der Kriterien:**

| Kriterium        | Punkte |
|------------------|--------|
| Mindestlänge     | 1      |
| Großbuchstaben   | 1      |
| Kleinbuchstaben  | 1      |
| Ziffer           | 1      |
| Sonderzeichen    | 2      |

**Maximale Punktzahl:** 6

**Stärkeklassen:**

| Punkte | Stärke     |
|--------|------------|
| 0–2    | `schwach`  |
| 3–4    | `mittel`   |
| 5–6    | `stark`    |

**Rückgabestruktur (Dictionary):**

```
{
    'mindestlaenge':       True/False,
    'grossbuchstaben':     True/False,
    'kleinbuchstaben':     True/False,
    'ziffer':              True/False,
    'sonderzeichen':       True/False,
    'erfuellte_kriterien': 0–5,
    'punkte':              0–6,
    'staerke':             'schwach' | 'mittel' | 'stark'
}
```

### 3.3 Passwort-Hashing

| ID    | Funktion          | Beschreibung                                               |
|-------|-------------------|------------------------------------------------------------|
| F-070 | `hash_passwort`   | Erzeugt einen SHA-256-Hash des Passworts und gibt ihn als 64-stelligen Hex-String zurück. Nutzt das Modul `hashlib` aus der Python-Standardbibliothek. |

### 3.4 Konsolenanwendung

| ID    | Beschreibung                                                          |
|-------|-----------------------------------------------------------------------|
| F-080 | Die Anwendung (`main.py`) bietet ein Menü mit den Optionen „Passwort prüfen" und „Beenden". |
| F-090 | Nach Eingabe eines Passworts werden alle Einzelergebnisse, die Punktzahl, die Stärkeklasse und der SHA-256-Hash formatiert ausgegeben. |
| F-100 | Ist `bewerte_passwort()` noch nicht implementiert, wird eine verständliche Fehlermeldung ausgegeben statt eines Programmabbruchs. |

---

## 4 Nichtfunktionale Anforderungen

| ID     | Kategorie       | Beschreibung                                             |
|--------|-----------------|----------------------------------------------------------|
| NF-010 | Modularität     | Alle Prüffunktionen liegen in `validator.py` als eigenständiges Modul. Das Modul hat keine Abhängigkeit zu `main.py`. |
| NF-020 | Testbarkeit     | Jede Funktion ist einzeln mit Unit Tests prüfbar. Die Tests liegen in `test_validator.py` und werden mit `pytest` ausgeführt. |
| NF-030 | Dokumentation   | Jede Funktion hat einen Docstring, der Zweck, Parameter und Rückgabewert beschreibt. |
| NF-040 | Lesbarkeit      | Der Code verwendet sprechende Variablen- und Funktionsnamen in deutscher Sprache. |
| NF-050 | Abhängigkeiten  | Das Modul nutzt ausschließlich die Python-Standardbibliothek (kein `pip install` nötig). |

---

## 5 Abgrenzung

Das Projekt umfasst **nicht**:

- Speicherung von Passwörtern in einer Datenbank
- Salting oder iteriertes Hashing (z. B. bcrypt, PBKDF2)
- Grafische Benutzeroberfläche
- Netzwerkkommunikation oder Benutzerverwaltung
- Prüfung gegen bekannte Passwortlisten (z. B. Have I Been Pwned)

---

## 6 Abnahmekriterien

| Nr. | Kriterium                                                               |
|-----|-------------------------------------------------------------------------|
| A1  | Alle Prüffunktionen (F-010 bis F-050) geben für gültige und ungültige Eingaben korrekte `bool`-Werte zurück. |
| A2  | `bewerte_passwort()` liefert ein Dictionary mit allen geforderten Schlüsseln und korrekten Werten. |
| A3  | `hash_passwort()` gibt für gleiche Eingaben identische und für verschiedene Eingaben unterschiedliche 64-stellige Hex-Strings zurück. |
| A4  | Alle automatisierten Tests (`python -m pytest test_validator.py -v`) bestehen.     |
| A5  | Die Konsolenanwendung gibt für die Testpasswörter aus dem Systemtest die erwarteten Stärkeklassen aus. |
