# Passwort-Validator – Projektübersicht

Diese Codebasis gehört zur Lernsituation **„Passwort-Validator"** im Fach
SuD. Der vollständige Arbeitsauftrag mit Niveaustufen
und Einzelaufgaben (A1, A2, B1, …) steht in
`docs/lernsituation_passwort_validator.md` – diese README beschreibt nur,
welche Dateien Sie vor sich haben und wie sie zusammenspielen.
Lesen Sie die Übersicht kurz durch und wechseln Sie dann in die Lernsituation.

---

## Die Dateien

Die Codebase (Python-Dateien) liegt im Hauptverzeichnis, alle didaktischen
Dokumente (Aufgabenstellung, Pflichtenheft, Testprotokoll usw.) finden Sie
unter `docs/`. Lehrer-interne Notizen liegen unter `docs/lehrer/`.

### `validator.py` – die eigene Bibliothek

Diese Datei ist das Herzstück des Projekts. Sie enthält ausschließlich
Funktionen zur Passwortprüfung – ähnlich wie Module aus der Python-Standardbibliothek
(`math`, `random`, `string`) stellt sie eine Sammlung von Funktionen bereit,
die von anderen Programmen importiert und genutzt werden können.

**Hier liegt Ihre Hauptarbeit:** Einige Funktionen sind fertig implementiert,
andere müssen Sie ergänzen.

> **Wichtig:** `validator.py` direkt auszuführen (`python validator.py`) ergibt
> keine Ausgabe – das ist korrekt und kein Fehler. Eine Bibliothek wird
> importiert, nicht direkt gestartet.

---

### `main.py` – die Anwendung

Diese Datei ist vollständig implementiert und muss für Niveau 1 und 2 nicht
verändert werden. (Nur in der optionalen Bonusaufgabe C3 darf `main.py`
erweitert werden, um die Entropie zusätzlich auszugeben.)
Sie importiert die Funktionen aus `validator.py` und stellt dem Nutzer
ein einfaches Menü zur Verfügung.

Starten mit:
```
python main.py
```

> **Hinweis:** `main.py` funktioniert erst vollständig, wenn Sie
> `bewerte_passwort()` und `hash_passwort()` in `validator.py` implementiert haben (Niveau 2).

---

### `test_validator.py` – die Testdatei

Diese Datei enthält automatisierte Tests für die Funktionen aus `validator.py`.
Einige Tests sind fertig, andere müssen Sie ergänzen.

Ausführen mit:
```
python -m pytest test_validator.py -v
```

Die Tests prüfen Ihre Implementierung automatisch und zeigen Ihnen sofort,
ob Ihr Code korrekt funktioniert.

---

### `docs/pflichtenheft_passwort_validator.md` – die Anforderungen

Das Pflichtenheft beschreibt formal, was das Modul können soll:
welche Funktionen es gibt, welche Parameter sie erwarten und welche
Ergebnisse sie liefern müssen. Nutzen Sie es als Nachschlagewerk,
wenn der Docstring im Code nicht ausreicht.

---

### `docs/testprotokoll_passwort_validator.md` – Ihr Testbericht

Eine leere Vorlage, in der Sie Ihre Testergebnisse dokumentieren –
sowohl die automatisierten Unit Tests als auch die manuellen Systemtests.
Füllen Sie das Protokoll begleitend zu den Aufgaben aus.

---

## Zusammenspiel der Dateien

```
test_validator.py                        Pflichtenheft
      │                                  (Anforderungen)
      │  importiert und testet                │
      ▼                                       ▼
validator.py  ◄──── importiert von ──── main.py
(Bibliothek)                          (Anwendung)
                                              │
                                              ▼
                                        Testprotokoll
                                       (Dokumentation)
```

`validator.py` weiß nichts von `main.py` oder `test_validator.py` –
das ist so gewollt. Eine gute Bibliothek funktioniert unabhängig davon,
wer sie benutzt. Das Pflichtenheft beschreibt, **was** gebaut werden soll,
das Testprotokoll dokumentiert, **ob** es funktioniert.

---

## Einrichtung (einmalig nach dem Clone)

Kurz:

```
python -m venv venv
venv\Scripts\activate          # Windows (bzw. source venv/bin/activate)
pip install -r requirements.txt
```

Ausführliche Anleitung (inkl. PowerShell-Hinweisen, VS Code und Schulrechnern):
`docs/howto_setup.md`.

---

## Schnellstart

1. Öffnen Sie `validator.py` und verschaffen Sie sich einen Überblick (Stellen mit `# TODO`).
2. Führen Sie die Tests einmal aus, um den Ausgangsstand zu sehen: `python -m pytest test_validator.py -v` – viele Tests werden rot sein, das ist der erwartete Ausgangsstand (= Ihre To-do-Liste), kein Fehler in Ihrer Installation. Einordnung der häufigsten Fehlermeldungen: `docs/howto_pytest.md` §3.
3. Folgen Sie ab hier den Aufgaben in `docs/lernsituation_passwort_validator.md` (Niveau 1 → 2 → 3) – dort sind Implementierung, Unit Tests, Systemtests und Testprotokoll strukturiert beschrieben.
