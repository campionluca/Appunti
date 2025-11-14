# Esercizi — 05 Server e Request

## Traccia
- Implementa un router minimale con due route (`/saluto`, `/saluto/json`).

## Requisiti
- Parsing di `REQUEST_URI` e risposta 404.

## Suggerimenti
- `parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH)`.

## Soluzione
- Vedi `../esempi/router.php`.
