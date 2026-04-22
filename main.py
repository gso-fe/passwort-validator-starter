# main.py
# Passwort-Validator – Hauptanwendung
# -------------------------------------------------------
# Diese Datei ist vollständig implementiert.
# Sie dient als Grundlage für den Systemtest (manuell).

from validator import bewerte_passwort, hash_passwort


def zeige_bewertung(ergebnis, pw_hash):
    """Gibt die Passwortbewertung formatiert auf der Konsole aus.

    Args:
        ergebnis (dict): Rückgabewert von bewerte_passwort().
        pw_hash (str):   SHA-256-Hash des Passworts.
    """
    CHECK = "✓"
    UNCHECK = "✗"

    print("\n┌──────────────────────────────────┐")
    print("│      Passwort-Analyse            │")
    print("├──────────────────────────────────┤")
    print(f"│  Mindestlänge (8 Zeichen): "
          f"  {CHECK if ergebnis['mindestlaenge'] else UNCHECK}   │")
    print(f"│  Großbuchstaben:           "
          f"  {CHECK if ergebnis['grossbuchstaben'] else UNCHECK}   │")
    print(f"│  Kleinbuchstaben:          "
          f"  {CHECK if ergebnis['kleinbuchstaben'] else UNCHECK}   │")
    print(f"│  Ziffern:                  "
          f"  {CHECK if ergebnis['ziffer'] else UNCHECK}   │")
    print(f"│  Sonderzeichen:            "
          f"  {CHECK if ergebnis['sonderzeichen'] else UNCHECK}   │")
    print("├──────────────────────────────────┤")
    print(f"│  Erfüllte Kriterien: "
          f"{ergebnis['erfuellte_kriterien']}/5         │")
    print(f"│  Punkte:             "
          f"{ergebnis['punkte']}/6         │")

    staerke = ergebnis['staerke'].upper()
    print(f"│  Passwortstärke:     {staerke:<12}│")
    print("├──────────────────────────────────┤")
    if pw_hash is not None:
        print(f"│  SHA-256-Hash:                   │")
        print(f"│  {pw_hash[:32]}│")
        print(f"│  {pw_hash[32:]}│")
    else:
        print(f"│  SHA-256-Hash: (nicht impl.)     │")
    print("└──────────────────────────────────┘\n")


def main():
    print("╔═════════════════════════════════╗")
    print("║      PASSWORT-VALIDATOR         ║")
    print("╚═════════════════════════════════╝")

    while True:
        print("1 - Passwort prüfen")
        print("2 - Beenden")
        auswahl = input("Auswahl: ").strip()

        if auswahl == "1":
            pw = input("Passwort eingeben: ")
            ergebnis = bewerte_passwort(pw)
            if ergebnis is None:
                print("Fehler: bewerte_passwort() ist noch nicht implementiert.\n")
            else:
                pw_hash = hash_passwort(pw)
                zeige_bewertung(ergebnis, pw_hash)
        elif auswahl == "2":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe - bitte 1 oder 2 eingeben.\n")


if __name__ == "__main__":
    main()
