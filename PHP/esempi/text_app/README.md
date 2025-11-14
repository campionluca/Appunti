# text_app — Elaborazione file di testo (stile C)

Vincoli rispettati:
- Niente `mb_*`, niente operatore `??`, niente funzioni regex, niente costanti `ENT_*`, niente specifica di codifica come `'UTF-8'`, nessuna dichiarazione di tipo di ritorno nelle funzioni.

Caratteristiche:
- I/O binario con `fopen('rb')`/`fopen('wb')`, lettura/scrittura a blocchi.
- Gestione manuale di buffer e puntatore (simulazione di `malloc/realloc/free`).
- Normalizzazione newline (CRLF/CR → LF) e sostituzione di byte non ASCII con `?` (opzionale).
- Escape HTML basilare senza costanti `ENT_*`.
- Gestione errori senza eccezioni: funzioni tornano oggetti risultato `{ ok, err, ... }`.

Struttura:
- `buffer.php`: buffer dinamico con capacità e statistiche di allocazione.
- `io.php`: wrapper per `fopen/fread/fwrite/fseek/ftell/fclose`.
- `encoding.php`: sanitizzazione ASCII, escape HTML, normalizzazione newline.
- `app.php`: script principale di elaborazione.

Uso CLI (se disponibile):
```
php app.php input_sample.txt output.txt
```

Uso via server PHP (se disponibile):
```
php -S localhost:8000 -t PHP/esempi
# Poi apri: http://localhost:8000/text_app/app.php?file=PHP/esempi/text_app/input_sample.txt
```

Note:
- La “gestione memoria” è simulata: PHP non espone puntatori crudi; tracciamo allocazioni e re-allocazioni.
- La “codifica” è gestita manualmente per ASCII; byte non ASCII sono sostituiti, senza librerie esterne.

