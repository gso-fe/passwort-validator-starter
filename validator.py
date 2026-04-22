# validator.py
# Passwort-Validator – Kernmodul
# -------------------------------------------------------
# Dieses Modul enthält Funktionen zur Passwortprüfung.
# Einige Funktionen sind fertig implementiert,
# andere müssen von euch ergänzt werden (markiert mit TODO).

import hashlib


def hat_mindestlaenge(passwort, mindestlaenge=8):
    """Prüft, ob das Passwort die Mindestlänge erfüllt.

    Args:
        passwort (str):      Das zu prüfende Passwort.
        mindestlaenge (int): Mindestanzahl Zeichen (Standard: 8).

    Returns:
        bool: True, wenn len(passwort) >= mindestlaenge, sonst False.

    Beispiele:
        >>> hat_mindestlaenge("abc")
        False
        >>> hat_mindestlaenge("abcdefgh")
        True
    """
    return len(passwort) >= mindestlaenge


def hat_grossbuchstaben(passwort):
    """Prüft, ob das Passwort mindestens einen Großbuchstaben enthält.

    Args:
        passwort (str): Das zu prüfende Passwort.

    Returns:
        bool: True, wenn mindestens ein Großbuchstabe vorhanden, sonst False.

    Algorithmus:
        1. Gehe jedes Zeichen im Passwort einzeln durch.
        2. Prüfe mit der Methode isupper(), ob das Zeichen ein Großbuchstabe ist.
        3. Sobald ein Großbuchstabe gefunden wird: gib True zurück.
        4. Wurde kein Großbuchstabe gefunden: gib False zurück.
    """
    for zeichen in passwort:
        if zeichen.isupper():
            return True
    return False


def hat_kleinbuchstaben( ):  # TODO Signatur: passenden Parameter ergänzen (siehe hat_grossbuchstaben)
    """Prüft, ob das Passwort mindestens einen Kleinbuchstaben enthält.

    Args:
        passwort (str): Das zu prüfende Passwort.

    Returns:
        bool: True, wenn mindestens ein Kleinbuchstabe vorhanden, sonst False.
    """
    # TODO: Implementiere diese Funktion.
    # Hinweis: Schau dir hat_grossbuchstaben() an – die Logik ist sehr ähnlich.
    # Verwende islower() statt isupper().
    pass


# TODO Signatur: Ersetzen Sie die gesamte def-Zeile unten durch eine eigene
# vollständige Funktionsdefinition. Orientieren Sie sich an der Signatur von
# hat_grossbuchstaben() oben. Die Funktion muss weiterhin "hat_ziffer" heißen,
# sonst finden die Tests sie nicht.
def hat_ziffer():  # <-- diese Zeile komplett durch Ihre Signatur ersetzen
    """Prüft, ob das Passwort mindestens eine Ziffer (0–9) enthält.

    Args:
        passwort (str): Das zu prüfende Passwort.

    Returns:
        bool: True, wenn mindestens eine Ziffer vorhanden, sonst False.

    Algorithmus:
        1. Gehe jedes Zeichen im Passwort einzeln durch.
        2. Prüfe mit der Methode isdigit(), ob das Zeichen eine Ziffer ist.
        3. Sobald eine Ziffer gefunden wird: gib True zurück.
        4. Wurde keine Ziffer gefunden: gib False zurück.
    """
    # TODO: Implementiere diese Funktion gemäß dem Algorithmus oben.
    pass


def hat_sonderzeichen(passwort):
    # TODO: Schreibe einen Docstring für diese Funktion.
    # Hinweis: Schau dir die Docstrings der anderen Funktionen als Vorlage an.
    SONDERZEICHEN = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

    for zeichen in passwort:
        if zeichen in SONDERZEICHEN:
            return True
    return False


def bewerte_passwort(passwort):
    """Bewertet ein Passwort anhand aller fünf Kriterien (gewichtet).

    Args:
        passwort (str): Das zu prüfende Passwort.

    Returns:
        dict: Ergebnisse aller Prüfungen sowie eine Gesamtbewertung.

    Rückgabe-Beispiel:
        {
            'mindestlaenge':       True,
            'grossbuchstaben':     False,
            'kleinbuchstaben':     True,
            'ziffer':              True,
            'sonderzeichen':       False,
            'erfuellte_kriterien': 3,
            'punkte':              3,
            'staerke':             'mittel'
        }

    Gewichtung der Kriterien:
        Mindestlänge     →  1 Punkt
        Großbuchstaben   →  1 Punkt
        Kleinbuchstaben  →  1 Punkt
        Ziffer           →  1 Punkt
        Sonderzeichen    →  2 Punkte   ← höhere Gewichtung!

        Maximale Punktzahl: 6

    Algorithmus:
        1. Rufe alle fünf Prüffunktionen auf und speichere die Ergebnisse
           als True/False in Variablen.
        2. Zähle, wie viele Kriterien True sind (erfuellte_kriterien, 0–5).
        3. Berechne die gewichteten Punkte:
             Addiere 1 Punkt je erfülltem Kriterium (Mindestlänge, Groß,
             Klein, Ziffer) und 2 Punkte wenn Sonderzeichen erfüllt ist.
        4. Bestimme die Stärke nach den Punkten:
             0–2 Punkte  →  'schwach'
             3–4 Punkte  →  'mittel'
             5–6 Punkte  →  'stark'
        5. Gib ein Dictionary mit allen Einzelergebnissen,
           erfuellte_kriterien, punkte und staerke zurück.
    """
    # TODO: Implementiere diese Funktion gemäß dem Algorithmus oben.
    # Rufe dazu die bereits vorhandenen Funktionen in diesem Modul auf.
    pass


def hash_passwort(passwort):
    """Erzeugt einen SHA-256-Hash des Passworts.

    In echten Anwendungen wird nie das Passwort selbst gespeichert,
    sondern nur sein Hash – ein digitaler Fingerabdruck, aus dem das
    ursprüngliche Passwort nicht zurückberechnet werden kann.

    Args:
        passwort (str): Das zu hashende Passwort.

    Returns:
        str: Der SHA-256-Hash als Hex-String (64 Zeichen lang).

    Beispiele:
        >>> hash_passwort("abc")
        'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
        >>> len(hash_passwort("beliebig"))
        64

    Algorithmus:
        1. Wandle das Passwort in Bytes um mit der Methode .encode().
           Hintergrund: Hashfunktionen arbeiten auf Byte-Ebene,
           nicht auf Strings. .encode() wandelt einen String in Bytes um.
        2. Erzeuge ein SHA-256-Hash-Objekt mit hashlib.sha256().
           Übergib die Bytes als Argument.
        3. Gib den Hash als lesbaren Hex-String zurück mit .hexdigest().

    Recherche-Hilfe:
        - Python-Dokumentation: https://docs.python.org/3/library/hashlib.html
        - Suchbegriffe: "python hashlib sha256 beispiel"
    """
    # TODO: Implementiere diese Funktion gemäß dem Algorithmus oben.
    # Du brauchst dafür das Modul hashlib, das oben importiert wird.
    # Die Lösung ist ein Einzeiler!
    pass
