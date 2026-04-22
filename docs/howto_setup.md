# HowTo: Python-Umgebung einrichten

**Thema:** `venv` und `pip install` für dieses Projekt
**Einmalig nach dem Clone** – danach genügt es, `venv` im Terminal zu aktivieren.

---

## 1 – venv anlegen

Im Projektverzeichnis (dort, wo `requirements.txt` liegt) ausführen:

```
python -m venv venv
```

Dadurch entsteht ein Ordner `venv/` mit einer eigenen Python-Installation.

---

## 2 – venv aktivieren

```
# Windows (cmd.exe)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

Nach erfolgreicher Aktivierung steht `(venv)` am Anfang der Prompt.

> **Windows/PowerShell-Fehler „Die Ausführung von Skripts ist … deaktiviert"?**
> Einmalig pro Benutzer erlauben:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
> Alternativ die `cmd.exe` statt PowerShell benutzen.

---

## 3 – Pakete installieren

```
pip install -r requirements.txt
```

Prüfen, ob pytest installiert ist:

```
python -m pytest --version
```

---

## 4 – VS Code

Bietet VS Code beim Öffnen des Projekts an, den Interpreter aus `venv`
zu nutzen, bestätigen Sie mit „Ja". Danach wird das `venv` automatisch
aktiviert, sobald Sie in VS Code ein neues Terminal öffnen.

---

## Was passiert hier eigentlich?

- **`venv` (Virtual Environment)** ist ein abgekapselter Ordner mit einer
  eigenen Python-Installation. So bleiben die Pakete dieses Projekts
  getrennt von Ihrer System-Python und von anderen Projekten – nichts
  wird global „verschmutzt".
- **`pip`** ist der Paketmanager von Python. Er lädt Pakete aus dem
  Python Package Index (PyPI) und installiert sie in das aktive `venv`.
- **`requirements.txt`** listet alle externen Pakete auf, die das Projekt
  braucht (hier nur `pytest`). `pip install -r requirements.txt`
  installiert genau diese Liste – so arbeitet die ganze Klasse mit
  demselben Stand.
