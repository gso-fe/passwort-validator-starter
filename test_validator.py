# test_validator.py
# Passwort-Validator – Automatisierte Tests
# -------------------------------------------------------
# Ausführen mit:  python -m pytest test_validator.py -v
#
# Aufbau:
#   Teil A: Unit Tests  – jede Funktion einzeln prüfen
#   Teil B: Integrationstests – bewerte_passwort() als Ganzes prüfen


import pytest
from validator import (
    hat_mindestlaenge,
    hat_grossbuchstaben,
    hat_kleinbuchstaben,
    hat_ziffer,
    hat_sonderzeichen,
    bewerte_passwort,
    hash_passwort,
)


# ================================================================
# TEIL A – UNIT TESTS
# ================================================================
# Jede Testklasse testet genau eine Funktion aus validator.py.
# Einige Tests sind bereits fertig, andere müsst ihr ergänzen.
# ----------------------------------------------------------------


class TestHatMindestlaenge:
    """Unit Tests für hat_mindestlaenge()"""

    def test_zu_kurz(self):
        assert hat_mindestlaenge("abc") == False

    def test_genau_mindestlaenge(self):
        assert hat_mindestlaenge("abcdefgh") == True

    def test_laenger_als_mindestlaenge(self):
        assert hat_mindestlaenge("abcdefghij") == True

    def test_leeres_passwort(self):
        assert hat_mindestlaenge("") == False

    def test_benutzerdefinierte_mindestlaenge(self):
        # Mindestlänge explizit auf 3 setzen
        assert hat_mindestlaenge("abc", mindestlaenge=3) == True


class TestHatGrossbuchstaben:
    """Unit Tests für hat_grossbuchstaben()"""

    def test_ein_grossbuchstabe_am_anfang(self):
        assert hat_grossbuchstaben("Hallo") == True

    def test_nur_kleinbuchstaben(self):
        assert hat_grossbuchstaben("hallo") == False

    def test_nur_grossbuchstaben(self):
        assert hat_grossbuchstaben("HALLO") == True

    def test_leeres_passwort(self):
        assert hat_grossbuchstaben("") == False

    def test_grossbuchstabe_in_der_mitte(self):
        assert hat_grossbuchstaben("haLlo") == True


class TestHatKleinbuchstaben:
    """Unit Tests für hat_kleinbuchstaben()"""

    def test_mit_kleinbuchstabe(self):
        assert hat_kleinbuchstaben("Passwort") == True

    def test_ohne_kleinbuchstabe(self):
        assert hat_kleinbuchstaben("PASSWORT") == False

    # TODO: Schreibe mindestens 2 weitere Testfälle.
    # Orientiere dich an TestHatGrossbuchstaben.
    # Denke an: gemischte Eingabe (Groß + Klein), leeres Passwort, nur Ziffern.


class TestHatZiffer:
    """Unit Tests für hat_ziffer()"""

    def test_mit_ziffer(self):
        assert hat_ziffer("Passwort1") == True

    def test_ohne_ziffer(self):
        assert hat_ziffer("Passwort") == False

    # TODO: Schreibe 3 weitere Testfälle.
    # Ideen: nur Ziffern, Ziffer am Anfang, leeres Passwort.

    pass


class TestHatSonderzeichen:
    """Unit Tests für hat_sonderzeichen()"""

    def test_mit_sonderzeichen(self):
        assert hat_sonderzeichen("Passw!rt") == True

    def test_ohne_sonderzeichen(self):
        assert hat_sonderzeichen("Passwort1") == False

    def test_leeres_passwort(self):
        assert hat_sonderzeichen("") == False

    # TODO: Schreibe 2 weitere Testfälle.
    # Ideen: mehrere Sonderzeichen, nur Sonderzeichen.

    pass


class TestHashPasswort:
    """Unit Tests für hash_passwort()"""

    def test_bekannter_hash(self):
        # SHA-256 von "abc" ist ein bekannter, nachprüfbarer Wert
        assert hash_passwort("abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"

    def test_gleiche_eingabe_gleicher_hash(self):
        assert hash_passwort("Test123!") == hash_passwort("Test123!")

    def test_verschiedene_eingaben_verschiedene_hashes(self):
        assert hash_passwort("passwort1") != hash_passwort("passwort2")

    def test_hash_laenge(self):
        # SHA-256 erzeugt immer einen 64 Zeichen langen Hex-String
        assert len(hash_passwort("beliebig")) == 64

    # TODO: Schreibe einen weiteren Testfall.
    # Ideen: leeres Passwort, sehr langes Passwort,
    #        Passwort mit Sonderzeichen/Umlauten.

    pass


# ================================================================
# TEIL B – INTEGRATIONSTESTS
# ================================================================
# Hier testen wir bewerte_passwort() als Ganzes.
# Die Funktion ruft intern alle Prüffunktionen auf –
# wir prüfen, ob das Ergebnis korrekt zusammengesetzt wird.
# ----------------------------------------------------------------


class TestBewertePaswort:
    """Integrationstests für bewerte_passwort()"""

    def test_rueckgabe_ist_dict(self):
        ergebnis = bewerte_passwort("Test123!")
        assert isinstance(ergebnis, dict)

    def test_alle_schluessel_vorhanden(self):
        ergebnis = bewerte_passwort("Test123!")
        erwartete_schluessel = [
            "mindestlaenge",
            "grossbuchstaben",
            "kleinbuchstaben",
            "ziffer",
            "sonderzeichen",
            "erfuellte_kriterien",
            "punkte",
            "staerke",
        ]
        for schluessel in erwartete_schluessel:
            assert schluessel in ergebnis, f"Schlüssel '{schluessel}' fehlt!"

    def test_schwaches_passwort(self):
        # "abc": nur Kleinbuchstaben erfüllt → 1 Punkt → schwach
        ergebnis = bewerte_passwort("abc")
        assert ergebnis["staerke"] == "schwach"
        assert ergebnis["punkte"] <= 2

    def test_starkes_passwort(self):
        # "Sicher#99!": alle 5 Kriterien, Sonderzeichen = 2 Punkte → 6 Punkte → stark
        ergebnis = bewerte_passwort("Sicher#99!")
        assert ergebnis["staerke"] == "stark"
        assert ergebnis["erfuellte_kriterien"] == 5
        assert ergebnis["punkte"] == 6

    def test_starkes_passwort_einzelwerte(self):
        ergebnis = bewerte_passwort("Sicher#99!")
        assert ergebnis["mindestlaenge"] == True
        assert ergebnis["grossbuchstaben"] == True
        assert ergebnis["kleinbuchstaben"] == True
        assert ergebnis["ziffer"] == True
        assert ergebnis["sonderzeichen"] == True

    # TODO: Schreibe einen Testfall für ein 'mittleres' Passwort (3–4 Punkte).
    # Tipp: Rechne die Punkte vorher manuell durch – die Gewichtung
    # (Sonderzeichen = 2 Punkte!) kann das Ergebnis überraschend beeinflussen.
    # Beispiel zum Nachrechnen: Was ergibt "Abcdefgh"? (Länge + Groß + Klein)

    pass


# ================================================================
# SYSTEMTEST-CHECKLISTE (manuell – nicht automatisiert)
# ================================================================
#
# Führt main.py aus und prüft folgende Szenarien manuell:
#
# Nr. | Eingabe          | Erwartetes Ergebnis
# ----|------------------|----------------------------------------------
#  1  | abc              | schwach, 0–2 Kriterien
#  2  | Abcdefgh         | mittel, Groß- + Klein- + Länge = 3
#  3  | Sicher#99!       | stark, alle 5 Kriterien
#  4  | (leere Eingabe)  | schwach, kein Kriterium erfüllt
#  5  | 12345678         | schwach (nur Ziffer + Länge = 2 Punkte)
#  6  | !@#$%^&*         | mittel (Länge + Sonderzeichen)
#
# Notiert eure Beobachtungen und vergleicht sie mit den
# automatisierten Testergebnissen.
# ================================================================
