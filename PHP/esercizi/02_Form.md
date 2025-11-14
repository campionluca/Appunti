# Esercizi — 02 Form HTML, GET/POST

## Traccia
- Implementa un form di contatto con POST.
- Valida email, mostra errore in caso di input non valido.
- Valida lato server e sanifica l'output.

## Requisiti
- Avvia server: `php -S localhost:8000 -t PHP/esempi`.
- Apri `http://localhost:8000/form.html`.

## Suggerimenti
- Leggi l’input da `$_POST['email'] ?? ''`.
- Valida la forma base con una regex, ad esempio: `preg_match('/^[^@\s]+@[^@\s]+\.[^@\s]+$/', $email)`.
- Escape output con `htmlspecialchars`.

## Soluzione
- Vedi `../esempi/processa.php` e `../esempi/form.html`.
