# HowTo: pytest

**Thema:** Automatisierte Tests in Python  
**Voraussetzung:** Python ist installiert, du arbeitest im Terminal / in der Eingabeaufforderung

---

## 1 – Installation

### Windows (eigener Rechner)

Öffne die **Eingabeaufforderung** (`cmd`) oder **PowerShell** und gib ein:

```
pip install pytest
```

Prüfe danach, ob die Installation geklappt hat:

```
pytest --version
```

Erwartete Ausgabe (Versionsnummer kann abweichen):

```
pytest 8.x.x
```

### Falls `pip` nicht gefunden wird

Python wurde vermutlich ohne PATH-Eintrag installiert. Versuche:

```
python -m pip install pytest
```

Oder installiere Python neu und setze beim Setup-Assistenten den Haken bei
**„Add Python to PATH"**.

### macOS / Linux

```
pip3 install pytest
```

---

## 2 – Kurzeinführung

### Was ist pytest?

pytest ist ein Framework, mit dem du Python-Code **automatisch testen** kannst.
Du schreibst Testfunktionen, pytest führt sie aus und meldet, ob alles
wie erwartet funktioniert – oder wo ein Fehler steckt.

### Dein erstes Beispiel

Angenommen, du hast eine Datei `rechner.py`:

```python
# rechner.py
def addiere(a, b):
    return a + b
```

Dazu schreibst du eine Testdatei `test_rechner.py`:

```python
# test_rechner.py
from rechner import addiere

def test_positive_zahlen():
    assert addiere(2, 3) == 5

def test_negative_zahl():
    assert addiere(-1, 4) == 3

def test_null():
    assert addiere(0, 0) == 0
```

Tests ausführen:

```
python -m pytest test_rechner.py -v
```

> **Tipp:** In diesem Kurs nutzen wir durchgängig `python -m pytest` statt nur
> `pytest`. Das funktioniert auch dann, wenn `pytest` nicht im PATH liegt.

Ausgabe bei Erfolg:

```
test_rechner.py::test_positive_zahlen   PASSED
test_rechner.py::test_negative_zahl     PASSED
test_rechner.py::test_null              PASSED

3 passed in 0.01s
```

### Was bedeutet `assert`?

`assert ausdruck` prüft, ob der Ausdruck `True` ergibt.
Ist er `False`, schlägt der Test fehl – pytest zeigt dann genau,
welcher Wert zurückkam und welcher erwartet wurde.

```python
assert addiere(2, 3) == 5   # ✓ kein Fehler
assert addiere(2, 3) == 9   # ✗ Test schlägt fehl
```

Fehlermeldung von pytest:

```
AssertionError: assert 5 == 9
```

### Namenskonventionen

pytest erkennt Tests automatisch, wenn du diese Regeln einhältst:

| Was           | Muss beginnen mit |
| ------------- | ----------------- |
| Dateiname     | `test_`           |
| Funktionsname | `test_`           |
| Klassenname   | `Test`            |

---

## 3 – Dein erster Testlauf in diesem Projekt

Wenn du `python -m pytest test_validator.py -v` zum ersten Mal ausführst, werden einige
Tests **grün** sein (`PASSED`) und viele **rot** (`FAILED`). Das ist der
erwartete Ausgangsstand – die roten Tests markieren genau die Stellen, an
denen du noch Code schreiben musst. Dein Job über die Lernsituation hinweg
ist, Stück für Stück mehr Tests grün zu bekommen.

Die drei häufigsten Fehlermeldungen beim Erstlauf in Klartext:

| Meldung                                                       | Was sie bedeutet                                                                                                                                   |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AssertionError: assert None == '...'`                        | Die Funktion hat noch nichts zurückgegeben (`pass` statt `return`). Sobald du den Rumpf implementierst, verschwindet der Fehler.                   |
| `TypeError: 'NoneType' object is not subscriptable`           | Der Test erwartet ein Dictionary, bekommt aber `None`. Gleiche Ursache: Funktion noch nicht implementiert.                                         |
| `TypeError: ... takes 0 positional arguments but 1 was given` | Die Funktion wird mit einem Argument aufgerufen, hat in ihrer Signatur aber keinen Parameter – ergänze den Parameter (siehe Niveau 1, Aufgabe A1). |

Wenn du eine Meldung siehst, die nicht in dieser Tabelle steht, liegt vermutlich
ein echter Fehler in deinem Code vor. Lies die Meldung dann genau: pytest zeigt
Datei, Zeilennummer und den fehlgeschlagenen `assert`.

---

## 4 – Cheat Sheet

### Tests ausführen

| Befehl                                              | Wirkung                                          |
| --------------------------------------------------- | ------------------------------------------------ |
| `python -m pytest`                                  | Alle Testdateien im Ordner ausführen             |
| `python -m pytest test_validator.py`                | Nur diese eine Datei ausführen                   |
| `python -m pytest test_validator.py -v`             | Mit ausführlicher Ausgabe (verbose)              |
| `python -m pytest test_validator.py -v -k "Ziffer"` | Nur Tests ausführen, die „Ziffer" im Namen haben |
| `python -m pytest --tb=short`                       | Kürzere Fehlermeldungen                          |

### Testergebnis-Symbole

| Symbol | Bedeutung                                     |
| ------ | --------------------------------------------- |
| `.`    | Test bestanden                                |
| `F`    | Test fehlgeschlagen (`assert` war False)      |
| `E`    | Fehler im Testcode selbst (z. B. ImportError) |
| `s`    | Test übersprungen (`@pytest.mark.skip`)       |

### Teststruktur

```python
# Einzelne Testfunktion (einfachste Form)
def test_beispiel():
    assert meine_funktion("eingabe") == "erwartetes_ergebnis"

# Testklasse (thematische Gruppierung)
class TestMeineFunktion:
    def test_fall_a(self):
        assert meine_funktion("a") == True

    def test_fall_b(self):
        assert meine_funktion("") == False
```

### Häufige assert-Muster

```python
assert ergebnis == True          # Gleichheit
assert ergebnis != "fehler"      # Ungleichheit
assert ergebnis is None          # Ist None
assert len(liste) == 3           # Länge prüfen
assert "schluessel" in dict      # Schlüssel vorhanden
assert isinstance(x, dict)       # Typ prüfen
```

### Tipp: Tests gezielt benennen

Gute Testnamen beschreiben, was getestet wird:

```python
# schlecht
def test_1():

# gut
def test_leeres_passwort_gibt_false_zurueck():
```

Das macht Fehlerausgaben sofort lesbar – auch Wochen später.

---

## 5 – Häufige Fehler

| Fehlermeldung                    | Ursache                                             | Lösung                                     |
| -------------------------------- | --------------------------------------------------- | ------------------------------------------ |
| `ModuleNotFoundError`            | Import-Pfad falsch oder Datei nicht gefunden        | Testdatei und Quelldatei im selben Ordner? |
| `pytest: command not found`      | pytest nicht installiert oder nicht im PATH         | `python -m pytest` versuchen               |
| `collected 0 items`              | Datei- oder Funktionsname beginnt nicht mit `test_` | Namenskonventionen prüfen (→ Abschnitt 2)  |
| `assert` schlägt unerwartet fehl | Funktion gibt `None` zurück (nicht implementiert)   | `pass` in der Funktion durch Code ersetzen |
