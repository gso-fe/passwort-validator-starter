# Lernsituation: Passwort-Validator

**Fach:** SuD · **Thema:** Funktionen, Modularisierung & Softwaretests in Python  
**Code-Dateien:** `validator.py` · `test_validator.py` · `main.py`  
**Begleitdokumente:** `pflichtenheft_passwort_validator.md` · `testprotokoll_passwort_validator.md`  
**Werkzeug:** pytest (`python -m pytest test_validator.py -v`)

---

## Betriebliches Szenario

Die **OHMega IT** entwickelt interne Werkzeuge für mittelständische Kunden.
Für ein neues Kundenportal soll ein Modul entstehen, das Benutzerpasswörter
bei der Registrierung automatisch auf Sicherheitskriterien prüft und bewertet.
Zusätzlich sollen Passwörter vor der Speicherung gehasht werden, damit sie
im Falle eines Datenlecks nicht im Klartext vorliegen.

Ihr Ausbilder hat Ihnen ein **Pflichtenheft** übergeben, das die Anforderungen
an das Modul beschreibt. Die Konsolenanwendung (`main.py`) und ein Grundgerüst
mit automatisierten Tests (`test_validator.py`) sind bereits vorbereitet –
Ihre Aufgabe ist die Implementierung und der Test der fehlenden Funktionen.

**Ihr Arbeitsauftrag:**

1. Implementieren Sie die fehlenden Prüffunktionen in `validator.py`
2. Schreiben und ergänzen Sie automatisierte Tests in `test_validator.py`
3. Führen Sie manuelle Systemtests durch und dokumentieren Sie Ihre Ergebnisse
   im Testprotokoll
4. Stellen Sie sicher, dass alle Anforderungen aus dem Pflichtenheft erfüllt sind

---

## Niveauübersicht

Die Lernsituation ist in drei Niveaustufen gegliedert.
Jedes Niveau baut auf dem vorherigen auf.

| Niveau           | Schwerpunkt                                               | Was Sie lernen                                                                                                                                                                              |
| ---------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Niveau 1** ✦   | Einstieg: Funktionen implementieren und Tests lesen       | Algorithmen in Python umsetzen, bestehende for-Schleifen mit Early-Return anwenden, pytest-Ausgaben interpretieren                                                                          |
| **Niveau 2** ✦✦  | Vertiefung: Komplexe Funktionen, Hashing und eigene Tests | Funktionskomposition (eine Funktion ruft andere auf), Dictionaries als Rückgabewert, externe Module recherchieren und nutzen (`hashlib`), Docstrings schreiben, eigene Unit Tests entwerfen |
| **Niveau 3** ✦✦✦ | Transfer: Testdesign und mathematische Vertiefung         | Testdaten bewusst wählen, Grenzfälle systematisch identifizieren, Passwortentropie berechnen                                                                                                |

---

## Materialien und Arbeitsweise

Das Modul `validator.py` enthält Funktionen zur Passwortprüfung. Einige Funktionen
sind bereits fertig implementiert, andere müssen Sie ergänzen (markiert mit `# TODO`).  
In `test_validator.py` sind automatisierte Tests vorbereitet – Sie führen sie aus,
lesen die Ergebnisse und ergänzen fehlende Testfälle.

> **Begleitdokumente:** Das Pflichtenheft (`pflichtenheft_passwort_validator.md`)
> beschreibt alle Anforderungen an das Modul – nutzen Sie es als Nachschlagewerk,
> wenn Sie wissen wollen, was eine Funktion genau tun soll. Im Testprotokoll
> (`testprotokoll_passwort_validator.md`) dokumentieren Sie Ihre Testergebnisse.

---

## Übersicht: Funktionen × Niveaustufen

Welche Funktion wird wann fertig? Die Tabelle zeigt, in welcher Stufe
jede Funktion in `validator.py` von „offen" auf „fertig" wechselt.

| Funktion (`validator.py`)               | Start | Niveau 1 | Niveau 2 | Niveau 3 |
| --------------------------------------- | ----- | -------- | -------- | -------- |
| `hat_mindestlaenge`                     | ☑     | —        | —        | —        |
| `hat_grossbuchstaben`                   | ☑     | —        | —        | —        |
| `hat_kleinbuchstaben`                   | ☐     | ☑        | —        | —        |
| `hat_ziffer`                            | ☐     | ☑        | —        | —        |
| `hat_sonderzeichen` (Rumpf / Docstring) | ☑ / ☐ | —        | — / ☑    | —        |
| `bewerte_passwort`                      | ☐     | —        | ☑        | —        |
| `hash_passwort`                         | ☐     | —        | ☑        | —        |
| `berechne_entropie` _(Bonus C3)_        | ☐     | —        | —        | ☑        |

_Legende:_ ☑ in dieser Stufe fertiggestellt · ☐ noch offen · — in dieser Stufe nicht Thema

---

## Vor dem Start: Orientierungsfragen

Bevor Sie mit der Implementierung beginnen: Beantworten Sie die folgenden
Fragen für sich (mündlich oder als Kurznotiz). Wenn Sie alle beantworten
können, sind Sie gut vorbereitet. Bei Unsicherheiten schlagen Sie in der
`README.md` oder in den obigen Abschnitten nach, öffnen Sie ggf. die Dateien unter `/docs` im Repository.

**Überblick & Dateien**

1. Welche drei Python-Dateien bilden die Codebasis, und welche Rolle hat jede davon (Bibliothek / Anwendung / Tests)?
2. Warum erzeugt `python validator.py` keine Ausgabe – und ist das ein Fehler?
3. In welcher Datei liegt Ihre Hauptarbeit, und woran erkennen Sie im Code die zu bearbeitenden Stellen?
4. Wofür nutzen Sie das Pflichtenheft, wofür das Testprotokoll – worin liegt der Unterschied?
5. Was können Sie tun, wenn Sie nicht wirklich verstehen was Unit-Tests sind und wie sie ausgeführt werden?

**Ablauf & Niveaustufen**

6. Was ist der erwartete Ausgangsstand, wenn Sie direkt nach dem Clone `python -m pytest test_validator.py -v` ausführen?
7. Warum liefert `python main.py` in Niveau 1 noch keine vollständige Ausgabe? Welche zwei Funktionen fehlen dafür?
8. In welcher Reihenfolge bearbeiten Sie die Niveaus, und welches Niveau erlaubt als einziges Änderungen an `main.py`?

---

## Pflichtaufgaben – Niveau 1 ✦

> Bearbeiten Sie diese Aufgaben als Einstieg. Sie sind Voraussetzung für alle höheren Niveaus.

### A1 – Funktionen implementieren

Öffnen Sie `validator.py`. Implementieren Sie die folgenden zwei Funktionen.
Bei beiden fehlt neben dem Rumpf auch ein Teil der **Signatur** – diesen
müssen Sie selbst ergänzen. Hinweise finden Sie jeweils im Code.

| Funktion              | Was zu tun ist                                                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `hat_kleinbuchstaben` | Parameter in der Signatur ergänzen **und** Funktionsrumpf schreiben. Kein Algorithmus vorgegeben – orientieren Sie sich an `hat_grossbuchstaben()`. Verwenden Sie `islower()` statt `isupper()`. |
| `hat_ziffer`          | **Komplette Signaturzeile** selbst schreiben (Vorlage: `hat_grossbuchstaben()`) und den Rumpf gemäß Algorithmus-Kommentar umsetzen.                                                              |

> **Tipp:** Die Funktion `hat_grossbuchstaben()` ist bereits fertig implementiert und
> dient Ihnen als Vorlage. Vergleichen Sie sie auch mit dem Beispiel aus der Einführung Funktionen.

**Kontrollieren Sie Ihre Implementierung** mit den bereits fertigen Unit Tests:

```
python -m pytest test_validator.py -v -k "Kleinbuchstaben or Ziffer"
```

Alle Tests dieser beiden Klassen müssen grün sein, bevor Sie weitermachen.

---

### A2 – Tests ausführen und lesen

Führen Sie alle vorhandenen Tests aus:

```
python -m pytest test_validator.py -v
```

Beantworten Sie schriftlich (Kommentar im Code oder kurze Notiz):

1. Wie viele Tests werden ausgeführt?
2. Welche Tests schlagen fehl – und warum?
3. Was bedeutet `PASSED` / `FAILED` / `ERROR` in der Ausgabe?

> **Hinweis zum Systemtest:** `python main.py` zu starten ergibt in Niveau 1 noch
> keine vollständige Ausgabe, weil `bewerte_passwort()` und `hash_passwort()` erst
> in Niveau 2 implementiert werden. Der manuelle Systemtest folgt daher in B5.

---

## Aufgaben – Niveau 2 ✦✦

> Voraussetzung: Alle Aufgaben aus Niveau 1 sind abgeschlossen.

### B1 – Docstring für `hat_sonderzeichen()` ergänzen

Die Funktion `hat_sonderzeichen()` ist bereits fertig implementiert,
hat aber noch keinen Docstring. Ergänzen Sie einen passenden Docstring –
orientieren Sie sich an den Docstrings der anderen Funktionen und an Ihrer Lösung
aus der Einführung Funktionen (Teil 2, Frage 6).

---

### B2 – `bewerte_passwort()` schrittweise implementieren

Die Funktion ist ein größerer Baustein – wir gehen sie in drei Schritten an.
Lesen Sie vor dem Start den Docstring der Funktion im Code sorgfältig durch.

#### B2a – Einzelprüfungen zusammenfassen

Rufen Sie in `bewerte_passwort()` alle fünf Prüffunktionen auf und legen Sie
ein Dictionary mit den fünf Booleans an (Schlüssel: `mindestlaenge`,
`grossbuchstaben`, `kleinbuchstaben`, `ziffer`, `sonderzeichen`).

Geben Sie das Dictionary zunächst direkt zurück. Führen Sie die Tests aus –
der Test `test_alle_schluessel_vorhanden` wird noch rot sein (die Aggregat-Schlüssel
`erfuellte_kriterien`, `punkte`, `staerke` fehlen), aber `test_rueckgabe_ist_dict`
und `test_starkes_passwort_einzelwerte` sollten bereits grün werden.

#### B2b – Gewichtete Punkte berechnen

Ergänzen Sie die Punktberechnung. **Achtung:** Sonderzeichen zählen doppelt
(2 Punkte), alle anderen Kriterien jeweils 1 Punkt. Maximale Punktzahl: 6.
Zählen Sie zusätzlich `erfuellte_kriterien` als reine Anzahl erfüllter Kriterien
(0–5, ohne Gewichtung). Erweitern Sie das Dictionary um beide Schlüssel.

#### B2c – Stärkeklasse bestimmen

Ergänzen Sie die Stärkeklasse (`'schwach'` / `'mittel'` / `'stark'`) nach den
Schwellen aus dem Docstring (0–2 / 3–4 / 5–6 Punkte). Fügen Sie den Schlüssel
`staerke` ins Dictionary ein und geben Sie das vollständige Dictionary zurück.

Nach B2c sollten alle Tests der Klasse `TestBewertePaswort` grün sein – mit
Ausnahme des TODO-Testfalls für ein „mittleres" Passwort (kommt in C1).

---

### B3 – `hash_passwort()` implementieren

Die Funktion nutzt das Modul `hashlib` aus der Python-Standardbibliothek.
Der Algorithmus steht als Kommentar im Code – **Sie müssen selbst recherchieren**,
wie `hashlib.sha256()` funktioniert. Hinweise und Links finden Sie im Docstring.

> **Hintergrund:** In echten Anwendungen wird nie das Passwort selbst gespeichert,
> sondern nur sein **Hash** – ein digitaler Fingerabdruck, aus dem das ursprüngliche
> Passwort nicht zurückberechnet werden kann.

---

### B4 – Fehlende Unit Tests schreiben

Öffnen Sie `test_validator.py`. Suchen Sie alle Stellen mit `# TODO` in Teil A.
Ergänzen Sie die fehlenden Testfälle:

- Klasse `TestHatKleinbuchstaben`: mindestens 2 weitere Testfälle
- Klasse `TestHatZiffer`: mindestens 3 weitere Testfälle
- Klasse `TestHatSonderzeichen`: mindestens 2 weitere Testfälle
- Klasse `TestHashPasswort`: mindestens 1 weiterer Testfall

**Hinweise zum Schreiben von Unit Tests:**

```python
def test_mein_testfall(self):
    assert meine_funktion("eingabe") == True   # oder False
```

- Testen Sie immer auch Grenzfälle: leerer String, nur Sonderzeichen, gemischte Eingaben.
- Ein Testfall pro `def test_...` – nicht mehrere Fälle in eine Methode packen.
- Dokumentieren Sie Ihre Testfälle im Testprotokoll (Teil A).

---

### B5 – Systemtest (manuell)

Starten Sie jetzt die Hauptanwendung:

```
python main.py
```

Testen Sie die folgenden Eingaben und tragen Sie die tatsächliche Ausgabe
im Testprotokoll (Teil C) ein:

| Nr. | Eingabe      | Erwartete Stärke |
| --- | ------------ | ---------------- |
| 1   | `abc`        | schwach          |
| 2   | `Abcdefgh`   | mittel           |
| 3   | `Sicher#99!` | stark            |
| 4   | _(leer)_     | schwach          |
| 5   | `12345678`   | schwach          |
| 6   | `!@#$%^&*`   | mittel           |

Füllen Sie anschließend Teil D (Zusammenfassung) im Testprotokoll aus und
beantworten Sie die Reflexionsfrage in Teil E:

> _Welchen Vorteil haben automatisierte Tests gegenüber dem manuellen Systemtest?
> Nennen Sie ein konkretes Beispiel aus dieser Aufgabe._

---

## Aufgaben – Niveau 3 ✦✦✦

> Voraussetzung: Alle Aufgaben aus Niveau 1 und 2 sind abgeschlossen.

### C1 – Integrationstest für mittleres Passwort

In `test_validator.py` fehlt ein Testfall in `TestBewertePaswort`
für ein **mittleres** Passwort (3 oder 4 Kriterien erfüllt).

- Wählen Sie ein geeignetes Passwort und begründen Sie kurz, warum es „mittel" ist.
- Schreiben Sie den Testfall vollständig selbst (kein TODO vorgegeben).
- Prüfen Sie: Liefert `bewerte_passwort()` den erwarteten Wert für `erfuellte_kriterien`?

---

### C2 – Eigene Testfälle für Randfälle

Überlegen Sie sich mindestens **zwei weitere Randfälle**, die noch nicht getestet werden.

Beispiele für Denkansätze (nicht alle müssen umgesetzt werden):

- Was passiert bei einem sehr langen Passwort (100 Zeichen)?
- Was passiert bei Leerzeichen im Passwort?
- Was passiert bei Umlauten (`ä`, `ö`, `ü`)?

Schreiben Sie je einen Unit Test und beschreiben Sie kurz, was Sie herausgefunden haben.

---

### C3 – Bonusaufgabe: Entropieberechnung ✦✦✦✦

Starke Passwörter lassen sich mathematisch messen. Die **Passwortentropie**
gibt an, wie viele Bits an Information ein Passwort enthält:

```
Entropie = Länge × log₂(Zeichenpoolgroesse)
```

Der Zeichenpool ergibt sich aus den Zeichenklassen, die im Passwort vorkommen:

| Zeichenklasse   | Größe |
| --------------- | ----- |
| Kleinbuchstaben | 26    |
| Großbuchstaben  | 26    |
| Ziffern         | 10    |
| Sonderzeichen   | 32    |

**Ihre Aufgabe:**

1. Implementieren Sie die Funktion `berechne_entropie(passwort)` in `validator.py`.
   Sie soll die Prüffunktionen aus dem Modul nutzen, um den Zeichenpool zu bestimmen,
   und dann die Entropie berechnen. Verwenden Sie `math.log2()`.

2. Schreiben Sie mindestens **drei Unit Tests** für `berechne_entropie()`.
   Überlegen Sie: Welche Werte können Sie rechnerisch vorhersagen?

3. Recherchieren Sie: Ab welcher Entropie gilt ein Passwort heute als sicher?
   Notieren Sie Ihre Quelle.

4. **Optional:** Geben Sie in `main.py` die Entropie zusätzlich zur Stärke aus.
   Für diesen Schritt müssen Sie die sonst unveränderte `main.py` anpassen –
   nur in C3 ist das ausdrücklich erlaubt.

---

## Abgabe

| Was                                 | Wo                                         |
| ----------------------------------- | ------------------------------------------ |
| Implementierter Code                | `validator.py`                             |
| Ergänzte Tests                      | `test_validator.py`                        |
| Ausgefülltes Testprotokoll          | `testprotokoll_passwort_validator.md`      |
| Schriftliche Antworten (A2, ggf. C) | Kommentare im Code oder separates Dokument |
| Screenshot: alle Tests grün         | Als Bilddatei                              |

> **Tipp für den Screenshot:** `python -m pytest test_validator.py -v` im Terminal ausführen
> und das Terminalfenster abfotografieren oder per Snipping Tool sichern.
