# Task Manager (Python HTTP)

Panoramica del sistema di gestione attività con backend Python e UI web minimal.

## Funzionalità principali

- CRUD completo per task: titolo, descrizione, priorità (`alta|media|bassa`), scadenza, assegnatario, progetto, stato (`da_fare|in_corso|completato`), tipo.
- Tracciamento: cronologia modifiche, time tracking (start/stop con durata), commenti.
- Interfaccia: vista elenco e Kanban, filtri avanzati (progetto, stato, priorità, tipo), ricerca, notifiche per scadenze imminenti.
- Backup JSON incrementale e sincronizzazione realtime (SSE) tra client.

## Avvio

```
python tools/tasks/server.py  # avvia su http://localhost:8003/
```

Apri `http://localhost:8003/index.html` per la UI.

## API

- `GET /api/tasks` → restituisce `{version, last_updated, tasks}`
- `POST /api/tasks` → crea task. Body JSON richiesto: `title, description, priority, deadline, assignee`. Facoltativi: `project, status, type`.
- `PUT /api/tasks/{id}` → aggiorna campi. Body JSON parziale con campi da aggiornare.
- `DELETE /api/tasks/{id}` → elimina task.
- `POST /api/tasks/{id}/start` → avvia sessione di time tracking.
- `POST /api/tasks/{id}/stop` → chiude ultima sessione di time tracking.
- `POST /api/tasks/{id}/comment` → aggiunge commento `{author, text}`.
- `GET /api/backup` → crea backup JSON e ritorna `{backup_path}`.
- `GET /api/events` → Server-Sent Events (SSE) per sincronizzazione realtime.

## Dati e formato

File database: `tools/tasks/tasks_db.json`

Struttura task minimo:

```
{
  "id": "abc123def456",
  "title": "Implementare kanban",
  "description": "UI con colonne e drag&drop",
  "priority": "alta",
  "deadline": "2025-11-15",
  "assignee": "Marco",
  "project": "PHP",
  "status": "in_corso",
  "type": "Sviluppo",
  "history": [ {"ts": "...", "action": "create", "by": "Marco" } ],
  "time_tracking": [ {"start": "...", "end": null, "duration_seconds": 0} ],
  "comments": [ {"author": "", "text": "", "ts": "..."} ],
  "created_at": "...",
  "updated_at": "..."
}
```

## Backup

- Percorso: `logs/task_backups/tasks_backup_YYYYMMDD_HHMMSS.json`
- Creazione: `GET /api/backup`
- Best practice: pianificare backup giornaliero; mantenere ultimi N (es. 30); integrare con sincronizzazione su storage esterno (es. cloud drive).

## Sincronizzazione realtime

- Meccanismo: SSE via `GET /api/events`.
- Il server emette eventi `update` su create/update/delete, time_start/stop, comment.
- Il client (`tools/tasks/web/app.js`) sottoscrive l’EventSource e ricarica la lista alla ricezione.
- Fallback: polling ogni 20s se SSE non disponibile.

## Notifiche scadenze

- La UI evidenzia e genera toast per task con scadenza entro 24 ore.
- Le notifiche sono de-duplicate per sessione (una per task).

## Sicurezza e scalabilità

- Single-user locale per semplicità (nessuna autenticazione). Per multiutente, integrare auth (JWT/sessioni) e autorizzazioni.
- Concorrenza: `ThreadingHTTPServer` con lock su DB.
- Persistenza: JSON file. Per volumi maggiori migrare a SQLite/PostgreSQL.

## Struttura

- Backend: `tools/tasks/server.py`
- UI: `tools/tasks/web/index.html`, `style.css`, `app.js`
- Database: `tools/tasks/tasks_db.json`
- Backup: `logs/task_backups/`

