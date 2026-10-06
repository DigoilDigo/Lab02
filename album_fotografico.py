import csv


def carica_da_file(file_path):
    album = {}
    with open(file_path) as o:
        reader = csv.DictReader(o, skipinitialspace=True)
        for row in reader:
            codice = row["codice"]
            album[codice] = {
                "titolo": row["titolo"],
                "autore": row["autore"],
                "mese": int(row["mese"]),
                "anno": int(row["anno"])
            }
    return album


def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    album[codice] = {
        "titolo": titolo,
        "autore": autore,
        "mese": mese,
        "anno": anno
    }
    return album[codice]


def cerca_foto(album, codice):
    return album.get(codice, None)


def elenco_foto_anno_per_titolo(album, anno):
    # Estraggo i titoli delle foto che corrispondono all'anno cercato
    titoli = [foto["titolo"] for foto in album.values() if foto["anno"] == anno]

    # Se non ci sono foto per quell'anno, restituisce niente
    if not titoli:
        return None

    # Restituisce la lista dei titoli ordinati alfabeticamente
    return sorted(titoli)


def stampa(album):
    print(album)


def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            stampa(album)
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()